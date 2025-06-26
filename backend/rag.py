from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-V2")
client = chromadb.Client()
collection = client.get_or_create_collection(name="study_docs")

def chunk_text(text, chunk_size=300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def embed_and_store(text):
    chunks = chunk_text(text)
    embeddings = model.encode(chunks)
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        collection.add(documents=[chunk], embeddings=[embedding], ids=[str(hash(chunk) + i)])

def retrieve_context(query, k=3):
    query_embedding = model.encode([query])[0]
    results = collection.query(query_embeddings=[query_embedding], n_results=k)
    return "\n".join(results["documents"][0])
