# 🩺 MedAssist — Medical AI Chatbot

MedAssist is a Retrieval-Augmented Generation (RAG) based medical chatbot built to answer general medical questions using information retrieved from a medical reference document.

I created this project to understand how different components of an AI application work together — from processing a medical document and generating embeddings to storing and retrieving information from a vector database and generating responses with an LLM.

> ⚠️ Disclaimer: MedAssist is intended for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

---

## 📌 About the Project

MedAssist uses Retrieval-Augmented Generation (RAG) to answer questions using information from a medical reference document.

Instead of relying only on the language model's existing knowledge, the application first searches the stored medical information for relevant content. The retrieved information is then provided to the language model to generate the response.

Example questions include:

- What is diabetes?
- What are the symptoms of hypertension?
- What is acne?
- What causes fever?

---

## 🧠 How It Works

The complete workflow is:

    Medical Reference PDF
            │
            ▼
        PDF Loading
            │
            ▼
       Text Splitting
            │
            ▼
    Hugging Face Embeddings
            │
            ▼
      Pinecone Vector DB
            │
            ▼
         Retriever
            │
            ▼
       User Question
            │
            ▼
      Retrieved Context
            │
            ▼
      Prompt + Context
            │
            ▼
         Groq LLM
            │
            ▼
      Generated Answer
            │
            ▼
        Flask Web UI

### In simple terms

1. A medical reference PDF is loaded.
2. The extracted text is divided into smaller chunks.
3. Each chunk is converted into an embedding.
4. The embeddings are stored in Pinecone.
5. A user asks a question through the web interface.
6. The application searches Pinecone for relevant information.
7. The most relevant chunks are retrieved.
8. The retrieved context is passed to the language model.
9. Groq generates the final response.
10. Flask sends the response back to the web interface.

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Backend

- Flask
- LangChain

### AI / RAG

- Hugging Face Sentence Transformers
- sentence-transformers/all-MiniLM-L6-v2
- Pinecone
- Groq
- LangChain retrieval chains

### Frontend

- HTML
- CSS
- JavaScript

---

## 🔎 RAG Pipeline

### 1. Document Loading

The application loads PDF documents from the Data directory using LangChain document loaders.

The project uses:

- PyPDFLoader
- DirectoryLoader

### 2. Text Splitting

The extracted medical content is divided into smaller chunks.

Current configuration:

- Chunk Size: 500
- Chunk Overlap: 20

Splitting the document into smaller pieces makes it easier to retrieve relevant information for a particular question.

### 3. Embeddings

The project uses the following Hugging Face model:

    sentence-transformers/all-MiniLM-L6-v2

The model converts the text chunks into numerical vectors.

These vectors allow the application to perform similarity-based searches.

### 4. Pinecone Vector Database

The generated embeddings are stored in Pinecone.

The project uses the following Pinecone index:

    test

The indexing process uses the Pinecone gRPC client.

The vector configuration is:

- Dimension: 384
- Metric: Cosine Similarity
- Cloud: AWS
- Region: us-east-1

### 5. Retrieval

When a user asks a question, the application searches the Pinecone vector database for similar content.

The retriever is configured to retrieve:

    Top 3 relevant chunks

These retrieved chunks are then used as context for the language model.

### 6. LLM Generation

The retrieved context is passed to the Groq language model through LangChain.

The project currently uses:

    openai/gpt-oss-20b

The system prompt instructs the model to use the retrieved context when answering the user's question and keep the response concise.

---

## 🌐 Flask Web Application

Flask is used as the backend web framework.

The main application is:

    app.py

The application provides the chatbot webpage through:

    /

User questions are processed through:

    /get

The frontend sends the user's message to the Flask backend.

Example request:

    {
        "msg": "What is diabetes?"
    }

The backend processes the question through the RAG pipeline and returns the generated response.

Example response:

    {
        "response": "..."
    }

The JavaScript frontend then displays the response inside the chatbot interface.

---

## 🎨 Frontend

The chatbot interface was created using HTML, CSS, and JavaScript.

The interface includes:

- 🩺 Medical-themed design
- 💬 Chat interface
- ⚡ Quick question buttons
- 🤖 AI assistant responses
- ⌨️ Enter-to-send functionality
- ⏳ Typing indicator
- 🟢 Online status
- 📱 Responsive layout
- ⚠️ Medical information disclaimer

The frontend communicates directly with the Flask backend to send questions and receive responses.

---

## 📁 Project Structure

The current GitHub repository contains:

    MedicalChatbot/
    │
    ├── research/
    │   └── trials.ipynb
    │
    ├── src/
    │   ├── __init__.py
    │   ├── helper.py
    │   └── prompt.py
    │
    ├── static/
    │   └── style.css
    │
    ├── templates/
    │   └── index.html
    │
    ├── app.py
    ├── store_index.py
    ├── template.py
    ├── setup.py
    ├── requirements.txt
    └── README.md

### Important Files

| File | Purpose |
|---|---|
| app.py | Main Flask application and RAG pipeline |
| store_index.py | Loads the medical PDF, creates embeddings, and stores vectors in Pinecone |
| src/helper.py | Handles PDF loading, text splitting, and Hugging Face embeddings |
| src/prompt.py | Contains the system prompt used by the RAG chain |
| templates/index.html | Chatbot webpage |
| static/style.css | Frontend styling |
| research/trials.ipynb | Notebook used during experimentation and development |
| template.py | Project setup utility |
| setup.py | Python package configuration |
| requirements.txt | Python dependencies |
| README.md | Project documentation |

---

## 📚 Medical Reference Data

The chatbot requires a medical reference PDF as its knowledge source.

During development, the medical reference document was stored locally inside:

    Data/

However, the medical reference PDF could not be uploaded to this GitHub repository because of the file-size limitation.

Therefore, the medical PDF is NOT included in this repository.

To run the complete indexing pipeline, place the medical reference PDF inside the local Data directory.

The expected local structure is:

    MedicalChatbot/
    │
    ├── Data/
    │   └── MedicalEncyclopedia.pdf
    │
    ├── research/
    ├── src/
    ├── static/
    ├── templates/
    │
    ├── app.py
    ├── store_index.py
    ├── setup.py
    └── requirements.txt

> Note: The medical reference PDF is intentionally not included in this GitHub repository.

---

## 🚀 How to Run

### 1. Clone the Repository

    git clone https://github.com/AniruddhaChaudhury2006/MedicalChatbot.git

Move into the project directory:

    cd MedicalChatbot

### 2. Create a Virtual Environment

On Windows:

    python -m venv venv

Activate it:

    venv\Scripts\activate

### 3. Install Dependencies

Install the project dependencies:

    pip install -r requirements.txt

If required by the environment, install the LangChain integration packages:

    pip install langchain-huggingface langchain-text-splitters langchain-groq langchain-classic

### 4. Configure API Keys

Create a .env file in the project root:

    PINECONE_API_KEY=your_pinecone_api_key
    GROQ_API_KEY=your_groq_api_key

### 5. Add the Medical PDF

Create the Data directory if it does not already exist:

    Data/

Place the medical reference PDF inside it:

    Data/
    └── MedicalEncyclopedia.pdf

The PDF is required for the document indexing process.

### 6. Build the Pinecone Index

Run:

    python store_index.py

The indexing process performs the following steps:

    Medical PDF
         ↓
    PDF Extraction
         ↓
    Text Splitting
         ↓
    Hugging Face Embeddings
         ↓
    Pinecone Vector Database

### 7. Start the Flask Application

Run:

    python app.py

The application will run on:

    http://192.168.0.184:8080

Open the address in your browser to use MedAssist.

---

## 🔐 API Key Security

API keys should never be published in a public GitHub repository.

Use environment variables instead:

    PINECONE_API_KEY=your_key
    GROQ_API_KEY=your_key

The .env file should remain private.

A .gitignore file should contain entries such as:

    .env
    venv/
    __pycache__/
    *.pyc

Never publish API keys inside:

- Python files
- Jupyter notebooks
- README files
- Screenshots
- GitHub repositories
- Public posts

---

## 🧪 Development Notebook

The project contains a Jupyter notebook:

    research/trials.ipynb

The notebook was used during the experimentation and development stages of the project.

It contains the work used to explore and test different parts of the AI/RAG pipeline.

---

## 💡 What I Learned

Building MedAssist gave me practical experience with several concepts involved in developing an AI application.

Some of the main concepts I worked with include:

- PDF document processing
- Text extraction
- Text chunking
- Embeddings
- Vector databases
- Similarity search
- Retrieval-Augmented Generation
- Prompt engineering
- LangChain
- Pinecone
- Hugging Face embeddings
- Groq LLM integration
- Flask
- Frontend/backend communication
- HTML
- CSS
- JavaScript
- Environment variables
- API key security

One of the most important things I learned from this project is that an LLM is only one part of a complete AI application.

The embedding model, vector database, retriever, prompt, LLM, backend, and frontend all have different responsibilities.

Connecting these components together helped me understand how a RAG-based application works from end to end.

---

## ⚠️ Limitations

MedAssist is an educational project and should not be considered a medical diagnostic or treatment system.

The quality of the responses depends on:

- The medical reference material
- PDF text extraction
- The retrieved context
- The embedding model
- The language model

The chatbot may therefore provide incomplete or incorrect information.

For actual medical concerns, users should consult a qualified healthcare professional.

---

## 🔮 Future Improvements

Some improvements I would like to explore in the future include:

- Adding more medical reference documents
- Displaying source information with each answer
- Adding conversation history
- Improving RAG evaluation
- Adding automated testing
- Improving error handling
- Adding authentication
- Deploying the application online
- Improving mobile responsiveness
- Improving source attribution
- Improving response evaluation

---

## 👨‍💻 About the Project

MedAssist is a hands-on AI/ML project created to explore how Retrieval-Augmented Generation can be used to build a domain-specific chatbot.

The project combines:

    Medical Knowledge
           +
    Text Embeddings
           +
    Vector Search
           +
    Retrieval
           +
    LLM
           +
    Flask
           +
    Web Interface

The main purpose of the project was to gain practical experience building an AI application from the document-processing stage all the way to a working web interface.

### Author

Aniruddha Chaudhury

---

## 📌 Important Note

The medical reference PDF is NOT included in this GitHub repository because it could not be uploaded due to its file size.

The PDF needs to be placed locally inside:

    Data/

before running:

    python store_index.py

The repository contains the application code, frontend, source modules, requirements, setup files, and development notebook.

---

⭐ Thanks for checking out MedAssist!
