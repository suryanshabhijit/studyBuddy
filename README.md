# studyBuddy
End to End backend server for your person AI-study-tutor

A FastAPI-based backend that enables semantic Q&A and automated flashcard generation from academic PDFs using a custom Retrieval-Augmented Generation (RAG) pipeline with SentenceTransformers, ChromaDB, and Together.ai's Mistral LLM.

---

## 🚀 Features

- Upload PDF notes/study material
- Semantic Question Answering using custom document context
- Auto-generation of revision-friendly flashcards
- Uses Together.ai LLM instead of OpenAI

---

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **LLM API**: Together.ai (Mistral 7B Instruct)
- **Embeddings**: SentenceTransformers (`all-MiniLM-L6-v2`)
- **Vector DB**: ChromaDB
- **PDF Parser**: pdfplumber
- **Other**: regex, Uvicorn, Python 3.10+

---

## 📡 API Endpoints

### 📄 `POST /upload`

Upload a PDF document. Extracts text, chunks it, embeds it, and stores it in ChromaDB for later retrieval.

- **Request**: `multipart/form-data`
  - `file`: PDF file to upload
- **Response**:  
  ```json
  {
    "message": "Document processed successfully"
  }


