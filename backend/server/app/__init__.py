from flask import Flask
from . import config
from flask_cors import CORS
from .vector_embedding.embeddings import load_embeddings, load_documents, generate_document_vectors
# from .vector_embedding.database import setup_database, query_similar_documents
from langchain.vectorstores.pgvector import PGVector

app = Flask(__name__)
# app.config.from_object(config)
CORS(app, origins=['http://localhost:3000'])

# Initialize pgvector database

DATABASE_URL = config.DATABASE_URL
DATABASE_NAME = config.DATABASE_NAME

embeddings = load_embeddings()
documents = load_documents("./vector_embedding/data")  
# document_vectors = generate_document_vectors(embeddings, documents)
db = PGVector.from_documents(
    embedding=embeddings,
    documents=documents,
    collection_name=DATABASE_NAME,
    connection_string=DATABASE_URL,
) 

from .routes import gpt_routes