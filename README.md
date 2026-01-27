# RAG-Based Question Answering System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system that allows users to upload documents and ask questions based on those documents. The system retrieves relevant document chunks using vector similarity and generates answers using a language model.

---

## Features
- Upload PDF and TXT documents  
- Automatic chunking and embedding generation  
- FAISS vector similarity search  
- Question answering using retrieved context  
- FastAPI backend  
- Web-based user interface  
- Background document ingestion  

---

## Tech Stack
- FastAPI  
- SentenceTransformers  
- FAISS  
- Transformers (Local LLM) / OpenAI API  
- HTML + JavaScript  

---

## Project Structure
```
app.py                # FastAPI entry point
background_tasks.py   # Document ingestion
ingestion.py          # Text extraction
chunking.py           # Document chunking
embeddings.py         # Embedding model
vector_store.py       # FAISS index
qa_service.py         # Retrieval + generation
templates/index.html  # Web UI
```

---

## Setup Instructions

### 1. Clone Repository
```
git clone https://github.com/YOUR_USERNAME/rag-document-qa.git
cd rag-document-qa
```

### 2. Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Run Server
```
uvicorn app:app --reload
```

### 5. Open in Browser
```
http://127.0.0.1:8000
```

---

## How It Works
1. User uploads document  
2. Background task extracts text  
3. Text is chunked and embedded  
4. Embeddings stored in FAISS  
5. User asks question  
6. Relevant chunks retrieved  
7. LLM generates final answer  

---

## Evaluation Points Covered
- Custom chunking strategy  
- Vector similarity retrieval  
- Background processing  
- API design with validation  
- Retrieval failure handling  
- Latency awareness  

---

## Deployment
The system can be deployed as a containerized FastAPI service. Lightweight deployments can run on platforms like Render, while heavier LLM-based versions are suitable for HuggingFace Spaces or cloud VM infrastructure.

---

## Author
Yogesh Kardile  
