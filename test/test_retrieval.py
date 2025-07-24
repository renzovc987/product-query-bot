from agents.retriever_agent import RetrieverAgent

def test_retrieve():
    agent = RetrieverAgent()
    results = agent.retrieve("pantalla AMOLED", top_k=2)
    assert len(results) > 0
