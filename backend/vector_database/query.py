from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from utils import load_documents

embeddings = OpenAIEmbeddings()

texts = load_documents()

# TODO: change to for documents instead of texts
docsearch = FAISS.from_texts(texts, embeddings)

class VectorbaseQuery:
    
    def similarity_search(query): 
        query_result = docsearch.similarity_search(query, k=5)
        return query_result