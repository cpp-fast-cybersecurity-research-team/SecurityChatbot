import os
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
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
    search_kwargs={'k': 1, 'fetch_k': 50}
)

api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0)

# Answer Question
qa_system_prompt = """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Respond in first person without any prefaces to the answer that mention your identity such as 'AI: or ChatGPT:'. If the context has nothing to do with the question, state that it isn't and do not answer the question. Use four sentences maximum and keep the answers concise, scientific, and professional. Keep responses in English. Here is the context: {context}"""

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
                "configurable": {"session_id": "4321"}
            },  # constructs a key "abc123" in `store`.
        )["answer"]
        print(gptResponse)
        return gptResponse