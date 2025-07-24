# 🧠 Product Query Bot (RAG Pipeline with FastAPI + LangChain + OpenRouter)

This project is a Retrieval-Augmented Generation (RAG) chatbot that receives user product queries and responds using information extracted from a local product document corpus.

Built with:
- **FastAPI** for the web API
- **LangChain** (modern modules)
- **FAISS** for vector similarity search
- **OpenRouter** as the LLM backend
- **HuggingFaceEmbeddings** for document indexing
- Optional: **Docker** for containerized execution

---

## 🚀 Features

- Accepts user queries via a POST endpoint (`/query`)
- Retrieves relevant product info using semantic search (FAISS)
- Generates natural language responses using a multi-agent structure
- Uses OpenRouter-compatible LLMs via API key
- Supports local and Docker deployment
- Swagger UI docs at `/docs`

---

## 📦 Requirements

- Python 3.10+
- OpenRouter account and API key: [https://openrouter.ai/keys](https://openrouter.ai/keys)
- Docker (optional, for containerized setup)

---

## 🛠️ Local Setup (Windows/Linux/macOS)

### 1. Clone or download the repo

```bash
git clone https://github.com/youruser/product-query-bot.git
cd product-query-bot
