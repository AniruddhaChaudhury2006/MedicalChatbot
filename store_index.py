from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
import os
from langchain_pinecone import PineconeVectorStore
from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from dotenv import load_dotenv
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY
data = r"C:\Users\Aniruddha Chaudhury\Documents\MedicalChatbot\Data"
extracted_data = load_pdf_file(data)
text_chunks = text_split(extracted_data)
embeddings = download_hugging_face_embeddings()
pc = Pinecone(api_key = "pcsk_6aiCki_CaSyz4Bj6e6RRogzezUSDAbDpmpHUhyecy31oUupqwRHhMwrmeFVGHcWyd4LWmD")
from pinecone import Pinecone, ServerlessSpec
index_name = "test"
if not pc.has_index(index_name):
    pc.create_index(name = index_name, dimension = 384, metric = "cosine", spec = ServerlessSpec(cloud = "aws", region = "us-east-1"))
docsearch = PineconeVectorStore.from_documents(documents = text_chunks, index_name = index_name, embedding = embeddings,)

