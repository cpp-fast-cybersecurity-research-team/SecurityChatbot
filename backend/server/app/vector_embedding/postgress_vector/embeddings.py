# Embeddings handling
from langchain.embeddings import OpenAIEmbeddings

def load_embeddings():
    return OpenAIEmbeddings()

def generate_document_vectors(embeddings, documents):
    return embeddings.embed_documents([t.page_content for t in documents])
