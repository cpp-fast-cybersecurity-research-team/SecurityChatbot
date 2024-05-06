import os
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import OpenAI
from . import config
from .vector_embedding.embeddings import load_embeddings, load_documents, generate_document_vectors
# from .vector_embedding.database import setup_database, query_similar_documents
from langchain.vectorstores.pgvector import PGVector
# from langchain_openai import OpenAIEmbeddings # Generate embeddings (vector respresentations) of text
# from langchain_community.vectorstores import FAISS # In-memory vector store implementation using FAISS
# from .routes import gpt_routes 
# from .vector_embedding.utils.embedding_utils import load_db # Get load database function load_db from utils.py

DATABASE_URL = config.DATABASE_URL
DATABASE_NAME = config.DATABASE_NAME

embeddings = load_embeddings()

print("Loading Documents...")
documents = load_documents("data/")
print("Documents Loaded Successfully")

#document_vectors = generate_document_vectors(embeddings, documents)
db = PGVector.from_documents(
    embedding=embeddings,
    documents=documents,
    collection_name=DATABASE_NAME,
    connection_string=DATABASE_URL,
) 

retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={'k': 2, 'fetch_k': 50}
)

api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0)

# Answer Question
qa_system_prompt = """You are an assistant for answering cybersecurity related questions. You will receive some context to answer the question. If you don't know the answer or if the context is irrelevant with the question, just say that you don't know. You will also receive a past conversation history to use a reference, but absolutely DON'T include 'AI:' or 'System:' at the beginning of your answers, and only respond with a response to the latest user question in first person, without any prefaces used beforehand. Use two to four sentences while keeping your answers concise, scientific, and professional. Keep responses in English. {context}"""

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", qa_system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)
question_answer_chain = create_stuff_documents_chain(llm, qa_prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Statefully manage chat history 
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

class GPTService:
    '''
        POST request for sending and receiving text to GPT API 

        Returns 201 for success
    '''
    def ReceiveResponse(message):
        gptResponse = conversational_rag_chain.invoke(
            {"input": message},
            config={
                "configurable": {"session_id": "1234"}
            },  # constructs a key "abc123" in `store`.
        )["answer"]
        print(gptResponse)
        return gptResponse