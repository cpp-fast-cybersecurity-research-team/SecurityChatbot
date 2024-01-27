import os
from dotenv import load_dotenv

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import tqdm
import glob

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

    for item_path in tqdm(glob(directory + "*.pdf")):
        doc_loader = PyPDFLoader(item_path)
        documents.extend(doc_loader.load_and_split(text_splitter=text_splitter))

    return documents

def load_db(embedding_function, save_path='faiss_db', index_name='documents'):
    '''
        Load vector database

        arg: embedding_function = embedding model, ex: OpenAI embedding
    '''
    db = FAISS.load_local(folder_path=save_path, index_name=index_name, embeddings = embedding_function)
    return db

def save_db(db, save_path='faiss_db', index_name='documents'):
    db.save_local(save_path, index_name)
    print("Saved db to " + save_path + index_name)