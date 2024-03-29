from langchain_community.vectorstores.faiss import FAISS
from langchain_openai import OpenAIEmbeddings
from utils import load_documents, save_db, load_db

embeddings = OpenAIEmbeddings()

db = load_db(embeddings)
db.add_documents(documents = load_documents("new_documents/"))
print("Index Updated")
save_db(db)