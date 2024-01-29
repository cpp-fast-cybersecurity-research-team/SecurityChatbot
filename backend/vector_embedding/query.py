from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from utils import load_db

embeddings = OpenAIEmbeddings()

documents = load_db(embeddings)

docsearch = FAISS.from_documents(documents, embeddings)

class VectorbaseQuery:
    
    def similarity_search(query): 
        query_result = docsearch.similarity_search(query, k=5)
        return query_result