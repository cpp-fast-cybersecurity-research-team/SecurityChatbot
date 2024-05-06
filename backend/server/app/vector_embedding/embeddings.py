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

    # TODO: change to pdf -> html -> html parser -> text
    for item_path in glob("*/vector_embedding/data/*.pdf"):
        doc_loader = PyPDFLoader(item_path)
        documents.extend(doc_loader.load_and_split(text_splitter=text_splitter))
    
        print("Loaded Document: " + item_path)

    print("Replacing NULL (0x00) characters...")
    for document in documents:
            document.page_content = document.page_content.replace('\x00', '')

    return documents

def load_embeddings():
    return OpenAIEmbeddings()

def generate_document_vectors(embeddings, documents):
    return embeddings.embed_documents([t.page_content for t in documents])
