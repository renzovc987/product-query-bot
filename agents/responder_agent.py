import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()

class ResponderAgent:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="nousresearch/deephermes-3-llama-3-8b-preview:free",  # Puedes cambiar el modelo aquí
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            openai_api_base=os.getenv("OPENAI_API_BASE")
        )

    def respond(self, query, context_docs):
        context = "\n".join([doc.page_content for doc in context_docs])
        prompt = f"""Usa el siguiente contexto para responder la pregunta del usuario:

{context}

Pregunta: {query}
Respuesta:"""
        return self.llm([HumanMessage(content=prompt)]).content
