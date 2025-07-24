from agents.retriever_agent import RetrieverAgent
from agents.responder_agent import ResponderAgent

retriever = RetrieverAgent()
responder = ResponderAgent()

def run_rag_pipeline(user_id, query):
    docs = retriever.retrieve(query)
    return responder.respond(query, docs)
