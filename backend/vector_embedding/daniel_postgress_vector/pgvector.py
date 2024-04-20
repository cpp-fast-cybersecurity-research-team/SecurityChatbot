from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader(r"C:\Users\vince\OneDrive\Documents\GitHub\SecurityChatbot\backend\vector_embedding\new_documents\Ch.01_Introduction_to_computers.pdf", encoding='utf-8')
documents = loader.load()

print(documents)  # prints the document objects
print(len(documents))  # 1 - we've only read one file/document into the loader

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
texts = text_splitter.split_documents(documents)

print(texts)
print(len(texts))

print(texts[0]) #temp viewing (comment out when finished)

embeddings = OpenAIEmbeddings()

vector = embeddings.embed_query('Testing the embedding model')

print(len(vector))  # 1536 dimensions

doc_vectors = embeddings.embed_documents([t.page_content for t in texts[:5]])

print(len(doc_vectors))  # 5 vectors in the output
print(doc_vectors[0])    # this will output the first chunk's 1539-dimensional vector

#   run the following commands in a new terminal to run the above code (after the app is running):
# pip install tiktoken

#   You should have docker desktop installed and open, then run the following in the terminal still:
# docker pull ankane/pgvector
# docker run --name pgvector -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d ankane/pgvector

#   note that name is the name of the current file, and password is whatever you set it to be,
#   the port is the port set up duing the envrionment setup

#   DataBase Setup:
# You can now install a GUI tool such as pgAdmin 4 to inspect the database that is running in the container, 
# or else use psql on the command-line. 
# If your using pgAdmin 4 then simply right click the server on the left and create a new server group named whatever you want.
# Then right click that server and register a server. The name can once again be whatever you want.
# In the connection section, you can specify the host as localhost, and the 
# password as whatever you used in the above command - mysecretpassword, in our case and save.

#   Using the right click query tool on your crated database (which you need to make next to the premade database and name vector_db), 
#   run the following code:
# CREATE DATABASE vector_db;
# CREATE EXTENSION pgvector;

#   run the following commands in the terminal:
# pip install psycopg2-binary pgvector

from langchain.vectorstores.pgvector import PGVector

CONNECTION_STRING = "postgresql+psycopg2://postgres:mysecretpassword@localhost:5432/vector_db"
COLLECTION_NAME = 'introduction_to_computers'

db = PGVector.from_documents(
    embedding=embeddings,
    documents=texts,
    collection_name=COLLECTION_NAME,
    connection_string=CONNECTION_STRING,
)

query = "What is AI capable of now"
similar = db.similarity_search_with_score(query, k=2)

for doc in similar:
    print(doc, end="\n\n")

vector = embeddings.embed_query(query)
print(vector)

#   in the database, go to the embedding table in your schema and run the following code:
# SELECT document, (embedding <=> vector) as cosine_distance #note that vector may need to be turned into a string
# FROM langchain_pg_embedding 
# ORDER BY cosine_distance
# LIMIT 2;

#   In addition to the above code you can also do the following:
# SELECT AVG(embedding) FROM langchain_pg_embedding;
