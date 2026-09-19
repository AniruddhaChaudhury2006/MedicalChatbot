from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
app = Flask(__name__)
load_dotenv()
PINECONE_API_KEY = 'pcsk_6aiCki_CaSyz4Bj6e6RRogzezUSDAbDpmpHUhyecy31oUupqwRHhMwrmeFVGHcWyd4LWmD'
GROQ_API_KEY = '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'
embeddings = download_hugging_face_embeddings()
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
os.environ['GROQ_API_KEY'] = GROQ_API_KEY
index_name = "test"
docsearch = PineconeVectorStore.from_existing_index(index_name = index_name, embedding = embeddings)
retriever = docsearch.as_retriever(search_type = 'similarity', search_kwargs = {'k' : 3})
llm = ChatGroq(model = "openai/gpt-oss-20b", temperature = 0.4, max_tokens = 500)
prompt = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", "{input}"),])
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/get', methods=['POST'])
def chat():
    data = request.get_json()
    msg = data['msg']
    print("Question:", msg)
    response = rag_chain.invoke({'input': msg})
    print("Response:", response['answer'])
    return jsonify({'response': response['answer']})
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)
