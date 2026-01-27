from ingestion import extract_text
from chunking import chunk_text
from embeddings import get_embeddings
from vector_store import add_to_index

def process_document(file):
    print("Processing document...")
    text = extract_text(file)

    if len(text.strip()) < 50:
        print("Document unreadable or empty")
        return

    print("Text extracted")

    chunks = chunk_text(text)
    print(f"Created {len(chunks)} chunks")

    embeddings = get_embeddings(chunks)
    print("Embeddings created")

    add_to_index(embeddings, chunks)
    print("Stored in FAISS")
