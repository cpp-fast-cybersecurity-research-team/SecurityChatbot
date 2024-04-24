# Database interaction
from langchain.vectorstores.pgvector import PGVector

def setup_database(connection_string, collection_name, embeddings, documents):
    db = PGVector.from_documents(
        embedding=embeddings,
        documents=documents,
        collection_name=collection_name,
        connection_string=connection_string,
    )
    return db

def query_similar_documents(db, query, k=2):
    return db.similarity_search_with_score(query, k)
