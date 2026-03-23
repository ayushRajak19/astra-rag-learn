# 🌟 Astra RAG Learn

A full-stack **Retrieval Augmented Generation (RAG)** application — built from scratch to deeply understand how modern GenAI systems work end to end.

> **Purpose:** Not just using frameworks — understanding every layer of a production RAG system including agents, backend API, frontend UI, and document ingestion pipeline.

---

## 🏗️ Project Architecture

```
astra-rag-learn/
├── src/
│   ├── agents_src/          ← AI Agents (parsing, matching, analysis)
│   ├── backend_src/         ← FastAPI REST API
│   ├── frontend_src/        ← React UI
│   └── rag_doc_ingestion/   ← Document chunking, embedding & indexing
├── docs_dir/                ← Sample documents for testing
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

```
User uploads document
        ↓
rag_doc_ingestion → chunk → embed → store in vector DB
        ↓
User asks a question
        ↓
Query embedded → semantic search → retrieve top-k chunks
        ↓
Chunks + question → LLM (Groq)
        ↓
Accurate, grounded answer
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **LLM** | Groq (llama-3.3-70b-versatile) |
| **Embeddings** | HuggingFace (BAAI/bge-small-en-v1.5) |
| **RAG Framework** | LlamaIndex |
| **Vector Database** | ChromaDB |
| **Backend** | FastAPI |
| **Frontend** | React |
| **Document Parsing** | PyMuPDF |
| **Environment** | Python 3.11 + uv |

---

## 📂 Module Breakdown

### `rag_doc_ingestion/`
Core RAG pipeline — the heart of the project.
- Load documents from `docs_dir`
- Chunk documents using semantic chunking
- Generate embeddings using HuggingFace models
- Store and retrieve from ChromaDB vector store

### `agents_src/`
AI agents that handle specific tasks:
- **Document Agent** — parse and understand documents
- **Query Agent** — process user questions
- **Analysis Agent** — generate structured insights

### `backend_src/`
FastAPI REST API exposing RAG capabilities:
- `POST /ingest` — upload and index documents
- `POST /query` — ask questions about documents
- `GET /health` — API health check

### `frontend_src/`
React UI for interacting with the RAG system:
- Document upload interface
- Chat-style Q&A interface
- Response with source citations

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11
- Node.js 18+
- Groq API key → https://console.groq.com

### Installation

```bash
# Clone the repo
git clone https://github.com/ayushRajak19/astra-rag-learn.git
cd astra-rag-learn

# Create virtual environment
py -3.11 -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install uv
uv pip install -r requirements.txt
```

### Environment Setup

Create a `.env` file in the root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### Run the Backend
```bash
cd src/backend_src
uvicorn main:app --reload --port 8000
```

### Run the Frontend
```bash
cd src/frontend_src
npm install
npm start
```

---

## 💡 Key Concepts Implemented

```
Chunking Strategy    → Semantic chunking for better retrieval
Embedding Model      → BAAI/bge-small-en-v1.5 (lightweight, accurate)
Similarity Search    → Cosine similarity via ChromaDB
Context Window       → Top-k chunk retrieval before LLM call
Hallucination Guard  → Grounded answers using only retrieved context
Agent Pattern        → Separate agents for separate responsibilities
```

---

## 🎯 What I Learned Building This

- Why RAG is better than fine-tuning for document Q&A
- How chunking strategy directly impacts retrieval quality
- Why cosine similarity works better than euclidean for text
- How to structure a production GenAI app with agents
- How to connect vector DB → LLM → REST API → React UI

---

## 🔗 Related Projects

| Project | Description |
|---|---|
| [Repo Copilot](https://github.com/ayushRajak19/repos-copilot-cb) | Ask anything about any GitHub codebase using RAG |
| [AI Resume Screener](#) | Match resumes to jobs using GenAI *(coming soon)* |

---

## 🚀 Tech Badges

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat&logo=python)
![LlamaIndex](https://img.shields.io/badge/LlamaIndex-RAG-purple?style=flat)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-green?style=flat)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=flat)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-teal?style=flat&logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-blue?style=flat&logo=react)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-yellow?style=flat)

---

## 👨‍💻 Author

**Ayush Rajak** — Aspiring GenAI Engineer

[![GitHub](https://img.shields.io/badge/GitHub-ayushRajak19-black?style=flat&logo=github)](https://github.com/ayushRajak19)

---

⭐ *Star this repo if it helped you understand RAG!*
