from langchain.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from utils import load_documents, save_db

embeddings = OpenAIEmbeddings
documents = load_documents("data/")

db = FAISS.from_documents(documents, embeddings)
print("Index Created")
save_db(db)