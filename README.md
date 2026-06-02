# 🚀 Enterprise RAG Application

A Production-Style Retrieval-Augmented Generation (RAG) application built using FastAPI, LangChain, Groq, Hugging Face Embeddings, FAISS, PostgreSQL, JWT Authentication, and Streamlit.

This project allows users to securely register, log in, upload PDF documents, and ask questions about the uploaded content using AI-powered semantic search and retrieval.

---

## 📌 Features

### Authentication & Security
- User Registration
- User Login
- JWT Authentication
- Password Hashing using bcrypt
- Protected API Endpoints

### RAG Pipeline
- PDF Upload
- PDF Parsing
- Document Chunking
- Hugging Face Embeddings
- FAISS Vector Store
- Semantic Search
- Context Retrieval
- AI-Powered Responses using Groq LLM

### Frontend
- Streamlit UI
- Login Page
- Registration Page
- PDF Upload Interface
- Chat-Based Question Answering
- Chat History

### Backend
- FastAPI REST APIs
- Layered Architecture
- Service-Based Design
- Middleware Support
- PostgreSQL Integration

---

## 🏗️ Architecture

```text
┌─────────────────────┐
│     Streamlit UI    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      FastAPI        │
│ Authentication APIs │
│      RAG APIs       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      LangChain      │
│ Document Processing │
│ Retrieval Pipeline  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ HuggingFace         │
│ Embeddings Model    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      FAISS DB       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Groq LLM       │
└─────────────────────┘
```

---

## 📂 Project Structure

```text
rag_project/
│
├── app/
│   ├── api/
│   │   ├── auth_routes.py
│   │   ├── rag_routes.py
│   │   └── health_routes.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── database.py
│   │   └── auth_dependency.py
│   │
│   ├── middleware/
│   │   └── logging_middleware.py
│   │
│   ├── models/
│   │   └── user_model.py
│   │
│   ├── schemas/
│   │   ├── auth_schema.py
│   │   └── rag_schema.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── rag_service.py
│   │   └── vector_service.py
│   │
│   └── main.py
│
├── streamlit_app/
│   └── app.py
│
├── uploaded_files/
├── faiss_index/
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT Authentication
- Passlib (bcrypt)

### AI / RAG
- LangChain
- Groq
- Hugging Face Embeddings
- FAISS

### Frontend
- Streamlit

### Utilities
- Python
- Pydantic
- Uvicorn

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory.

```env
DATABASE_URL=postgresql://postgres:password@localhost/ragdb

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

GROQ_API_KEY=your_groq_api_key
```

---

## 🚀 Run FastAPI Server

```bash
python -m uvicorn app.main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## 🎨 Run Streamlit UI

```bash
streamlit run streamlit_app/app.py
```

Streamlit UI:

```text
http://localhost:8501
```

---

## 🔄 Application Flow

### User Authentication

1. Register Account
2. Login
3. Receive JWT Token
4. Access Protected APIs

### RAG Workflow

1. Upload PDF
2. Extract Text
3. Split into Chunks
4. Generate Embeddings
5. Store in FAISS
6. Ask Questions
7. Retrieve Relevant Chunks
8. Generate Answer using Groq
   
---

## 🔮 Future Enhancements

- Multi-PDF Support
- Document Management
- User-Specific Vector Stores
- Chat Memory
- Streaming Responses
- Docker Support
- Kubernetes Deployment
- Redis Caching
- Pinecone / Weaviate Integration
- Role-Based Access Control (RBAC)

---

## 👨‍💻 Author

CHARAN REDDY KALICHETI

LinkedIn: https://www.linkedin.com/in/charan-reddy-kalicheti-421b53242/?skipRedirect=true


---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.
