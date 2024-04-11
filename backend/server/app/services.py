import os

from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings # Generate embeddings (vector respresentations) of text
from langchain_community.vectorstores import FAISS # In-memory vector store implementation using FAISS
from backend.server.app.routes import gpt_routes 
from backend.vector_embedding.utils import load_db # Get load database function load_db from utils.py

# Load the vector store using load_db
embeddings = OpenAIEmbeddings()
vector_store = load_db(embeddings)

api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0)

# Templates
template = """The following is a friendly conversation between a human and an AI. The AI uses simple language and is straight to the point. If the AI does not know the answer to a question, it truthfully says it does not know.

Current conversation:
{history}
Human: {input}
AI Assistant:"""

# PROMPT = PromptTemplate(input_variables=["history", "input"], template=template)

# Replace previous conversation chain with conversation retriever chain

retriever = vector_store.as_retriever()

# Conversation Chain replaced with Conversational Retrieval Chain
conversational_retrieval_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    verbose=True,
    memory=ConversationBufferMemory(ai_prefix="AI Assistant"),
)

# Replace conversation with the created conversation_retrieval_chain
class GPTService:
    '''
        POST request for sending and receiving text to GPT API 

        Returns 201 for success
    '''
    def ReceiveResponse(message):
        gptResponse = conversational_retrieval_chain.predict(input=message)
        print(gptResponse)
        return gptResponse