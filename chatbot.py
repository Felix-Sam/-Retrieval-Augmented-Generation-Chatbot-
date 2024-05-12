from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_pinecone import PineconeVectorStore
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')
MODEL = 'gpt-3.5-turbo'
model = ChatOpenAI(api_key=API_KEY,model=MODEL)

parser = StrOutputParser()

telesam_key = os.getenv('telesam_key')
model_grok = ChatGroq(api_key =telesam_key,model_name = 'gemma-7b-it')
print(telesam_key )

loader = TextLoader('data.txt',encoding = 'utf-8')
document = loader.load()
document_spliter = RecursiveCharacterTextSplitter(chunk_size=2000,chunk_overlap = 500)
data = document_spliter.split_documents(document)

template = ("""
You are AI-powered chatbot designed to provide information and assistance for customers
based on the context provided to you only. In case you don't know what user's are 
requesting for just let them know. Note do not start answers with The provided text contains nor end with it.
Context:{context}
Question:{question}
""")

prompt = PromptTemplate.from_template(template=template)
prompt.format(
    context = ' Here is a context to use',
    question = ' This is a question to answer'
)

# # For sending the data to the database. it should be run only once.
# pinecone_index_name = 'telesam'
# embeddings = OpenAIEmbeddings()
# pinecone = PineconeVectorStore.from_documents(data,embedding=embeddings,index_name = pinecone_index_name)

# For retrieving data from the database.
pinecone_index_name = 'telesam'
embeddings = OpenAIEmbeddings()
pinecone = PineconeVectorStore(embedding=embeddings,index_name = pinecone_index_name)

retriever = pinecone.as_retriever()
result = RunnableParallel(context =retriever,question = RunnablePassthrough())
chain = result |prompt | model_grok | parser


app  = FastAPI()
class Data(BaseModel):
    text: str 

@app.post('/prompt')
async def prompts(data:Data):
    response = chain.invoke(data.text)
    return {'response': response}

@app.post('/add_data')
async def add_data(data:Data):
    try:
        pinecone.add_texts([data.text])
        return 'sucessfully added'
    except:
        return 'failed to add data'
    


