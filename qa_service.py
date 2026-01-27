from transformers import pipeline
from embeddings import model
from vector_store import search

generator = pipeline("text-generation", model="google/flan-t5-base")

def answer_question(question):
    q_embedding = model.encode([question])[0]
    context_chunks = search(q_embedding)

    if not context_chunks:
        return "No relevant information found."

    context = "\n".join(context_chunks)

    prompt = f"Answer the question using this context:\n{context}\nQuestion: {question}"

    result = generator(prompt, max_length=200)
    return result[0]["generated_text"]
