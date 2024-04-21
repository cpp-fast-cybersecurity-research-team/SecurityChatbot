import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from tqdm import tqdm
from glob import glob

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# TODO: take in parameters for file path
def load_documents(directory : str):
    '''
        Loads documents from specified directory and return list of document objects

        args: directory format = directory/
    '''

    documents = []

    # Basic text splitter
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function = len,
    )

    for item_path in glob("**/" + directory + "*.pdf"):
        doc_loader = PyPDFLoader(item_path)
        documents.extend(doc_loader.load_and_split(text_splitter=text_splitter))

    return documents

def load_db(embedding_function, save_path='backend/vector_embedding/faiss_db', index_name='documents'):
    '''
        Load vector database with FAISS

        arg: embedding_function = embedding model, ex: OpenAI embedding
    '''
    db = FAISS.load_local(folder_path=save_path, index_name=index_name, embeddings = embedding_function, allow_dangerous_deserialization=True)
    return db

def save_db(db, save_path='vector_embedding/faiss_db', index_name='documents'):
    '''
        Save vector database locally with FAISS

        arg: db = vector database
    '''
    db.save_local(save_path, index_name)
    print("Saved db to " + save_path + index_name)