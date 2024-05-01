import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from tqdm import tqdm
from glob import glob
from langchain.embeddings import OpenAIEmbeddings

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

def load_embeddings():
    return OpenAIEmbeddings()

def generate_document_vectors(embeddings, documents):
    return embeddings.embed_documents([t.page_content for t in documents])