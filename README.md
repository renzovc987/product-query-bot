# 🧠 Product Query Bot (RAG Pipeline with FastAPI + LangChain + OpenRouter)

This project is a Retrieval-Augmented Generation (RAG) chatbot that receives user product queries and responds using context extracted from a local product document corpus.

Built with:
- **FastAPI** for the REST API
- **LangChain** with modular components
- **FAISS** for semantic document retrieval
- **HuggingFace Embeddings** for vectorization
- **OpenRouter** for LLM responses
- **Docker** support for containerization

## 🛠️ Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/product-query-bot.git
cd product-query-bot
python -m venv venv
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

## 🐳 Run with Docker

```bash
docker build -t product-query-bot .
docker run --env-file .env -p 8000:8000 product-query-bot
```

## 🧪 Test the API

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"user_id": "u001", "query": "Which product has AMOLED screen?"}'
```

## 📄 License

MIT License © 2024


