from fastapi import FastAPI, UploadFile, File, Query
from rag import embed_and_store, retrieve_context, chunk_text
from flashcards import generate_flashcards
from together_llm import generate_answer
import pdfplumber
import io

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        # Read the raw bytes from the uploaded PDF (async)
        contents = await file.read()

        # Wrap the bytes in an in-memory buffer for pdfplumber
        with pdfplumber.open(io.BytesIO(contents)) as pdf:
            text = "\n".join([
                page.extract_text() for page in pdf.pages if page.extract_text()
            ])
        
        if not text.strip():
            return {"error": "No text found in the PDF"}

        # Embed into ChromaDB
        embed_and_store(text)
        return {"message": "Document processed successfully"}

    except Exception as e:
        return {"error": f"Failed to process PDF: {str(e)}"}

@app.get("/ask")
def ask_question(q: str = Query(...)):
    context = retrieve_context(q)
    prompt = f"Context:\n{context}\n\n Question: {q}"
    answer = generate_answer(prompt)
    return {"answer": answer}

@app.post("/flashcards")
def flashcards_from_text(payload: dict):
    text = payload.get("text","")
    chunks = chunk_text(text)
    flashcards = [generate_flashcards(chunk) for chunk in chunks]
    return {"flashcards":flashcards}