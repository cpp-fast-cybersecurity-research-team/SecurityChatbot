 # Configuration settings

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("PGVECTOR_CONNECTION_STRING")
DATABASE_NAME = os.getenv("PGVECTOR_COLLECTION_NAME")
