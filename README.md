# 📚 RAG-Based Document Question Answering System

A full-stack **Retrieval-Augmented Generation (RAG)** application that allows users to upload documents and ask natural language questions. The system retrieves relevant content using vector similarity search and generates accurate answers using a language model.

🔗 **Live Demo:** https://huggingface.co/spaces/Yogesh942134/rag-document-qa

---

## 🚀 What This Project Does

Instead of relying only on a language model’s internal knowledge, this system:

1. Accepts user-uploaded documents  
2. Converts document text into vector embeddings  
3. Stores them in a high-performance vector database  
4. Retrieves the most relevant document chunks  
5. Generates answers grounded in the uploaded content  

This enables **context-aware, document-specific question answering**.

---

## 🧠 Key Features

- 📄 Upload **PDF** and **TXT** files  
- ✂️ Intelligent document **chunking with overlap**  
- 🔢 Embedding generation using SentenceTransformers  
- ⚡ Fast similarity search with FAISS  
- 🤖 Answer generation using:
  - Local Transformer models  
  - Or external APIs like OpenAI  
- 🌐 Interactive Web Interface  
- 🔄 Background document processing  
- 🧩 Modular backend architecture  

---

## 🏗️ System Architecture

**Pipeline Flow:**

**User Document → Text Extraction → Chunking → Embeddings → FAISS Index → Query → Retrieval → LLM → Answer**

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Backend API | FastAPI |
| Embeddings | SentenceTransformers |
| Vector Search | FAISS |
| Language Model | Hugging Face Transformers / OpenAI API |
| Frontend | HTML + JavaScript |
| Deployment | HuggingFace Spaces / Cloud / Containers |

---

## 📂 Project Structure

```
app.py                # FastAPI application entry
background_tasks.py   # Async document ingestion
ingestion.py          # Text extraction from files
chunking.py           # Document chunking logic
embeddings.py         # Embedding model wrapper
vector_store.py       # FAISS index management
qa_service.py         # Retrieval + answer generation
templates/index.html  # Web interface
```

---

## ⚙️ Installation

```bash
git clone https://github.com/Yogesh942134/rag-document-qa.git
cd rag-document-qa

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
uvicorn app:app --reload
```

Then open:  
👉 http://127.0.0.1:8000

---

## 🔍 How Retrieval Works

- Documents are split into ~**500-character chunks with overlap**
- Each chunk is converted into a dense vector embedding
- User queries are embedded into the same vector space
- **Similarity search** retrieves top-k relevant chunks
- The LLM generates answers using only retrieved context

This improves:
- Accuracy  
- Factual grounding  
- Domain adaptation  

---

## ⚡ Performance Considerations

- Background processing prevents UI blocking  
- FAISS enables fast large-scale similarity search  
- Cold start latency mainly from model loading  
- Designed for scalable document-based AI systems  

---

## 🌍 Deployment Options

This project can be deployed on:

- HuggingFace Spaces (recommended for demos)
- Cloud VM (for local LLM hosting)
- Containerized FastAPI service
- Render / Railway for API-based versions

---

## 🎯 Use Cases

- Research paper Q&A  
- Legal or policy document search  
- Internal company knowledge base  
- Educational material assistant  
- Resume / report analysis  

---
