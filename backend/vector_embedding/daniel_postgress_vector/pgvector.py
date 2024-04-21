from embeddings import load_embeddings, generate_document_vectors
from database import setup_database, query_similar_documents
import config

def main():
    embeddings = load_embeddings()
    documents = ...  # Load or define your documents here
    document_vectors = generate_document_vectors(embeddings, documents)
    
    # Replace "collection_name_here" and "Your query here" with actual values as needed.
    db = setup_database(config.DATABASE_URL, "collection_name_here", embeddings, document_vectors)
    similar_documents = query_similar_documents(db, "Your query here")

    for doc in similar_documents:
        print(doc)

if __name__ == "__main__":
    main()