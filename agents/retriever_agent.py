import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()

class RetrieverAgent:
    def __init__(self):
        self.vector_store = self._load_vector_store()

    def _load_vector_store(self):
        loader = DirectoryLoader("data/products", glob="**/*.txt")
        documents = loader.load()
        splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = splitter.split_documents(documents)
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        return FAISS.from_documents(docs, embeddings)

    def retrieve(self, query, top_k=3):
        return self.vector_store.similarity_search(query, k=top_k)
