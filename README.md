This project implements an AI-powered chatbot using LangChain, OpenAI GPT-3.5 Turbo, and 
ChatGroq's gemma-7b-it model. The chatbot processes customer queries based on 
provided context and can retrieve data from a vector database. It also includes a 
feature to convert text responses to speech using the UnrealSpeech API.

The project includes two components:

Chatbot Backend (FastAPI): Handles incoming user requests, retrieves relevant context from the Pinecone vector database, 
and generates a response using AI models.
Frontend Interface (Streamlit): Provides a user-friendly interface to interact with the chatbot, displays 
the bot's replies, and generates audio responses using text-to-speech functionality.

Table of Contents
Installation
Project Structure
How It Works
Usage
Customization
Dependencies
License

Installation
Clone the Repository
Open your terminal and run:
git clone <repository_url>
cd <repository_directory>

Install Dependencies
Make sure you have Python installed. Install the required packages using:
pip install -r requirements.txt
Environment Variables
Create a .env file in the project root and add your API keys:
OPENAI_API_KEY=<Your_OpenAI_API_Key>
telesam_key=<Your_TeleSam_API_Key>
Project Structure


├── chatbot.py                  # Backend API using FastAPI for chatbot
├── testapp.py                  # Streamlit frontend interface for chatbot
├── data.txt                    # Sample data used for embedding storage
├── requirements.txt            # Dependencies for the project
├── model.pkl                   # Trained machine learning model for context retrieval
└── .env                        # API keys for OpenAI and TeleSam


How It Works
1. Backend API (chatbot.py)
The FastAPI backend receives user prompts via POST requests. It performs the following steps:

Retrieves the relevant context from Pinecone vector database.
Uses ChatGroq or OpenAI GPT-3.5 Turbo to generate responses based on the context.
Sends the response back to the client.
Key components include:

LangChain's ChatOpenAI: Handles the interaction with OpenAI's GPT model.
LangChain's PineconeVectorStore: Manages document retrieval using embeddings.
TextLoader & TextSplitter: Prepares text data for embedding storage.
2. Frontend Interface (testapp.py)
The Streamlit app provides a simple UI for users to interact with the chatbot. 
It sends user input to the backend and displays the chatbot's response. It also includes 
text-to-speech conversion using the UnrealSpeech API.

Key components:

Streamlit: A framework to create a web interface.
Requests: Used to send and receive data from the chatbot backend.
Text-to-Speech: Converts the chatbot's reply into an audio response using UnrealSpeech.
Usage
Backend (FastAPI)
Start the Backend Server Run the chatbot.py script to launch the FastAPI server:
uvicorn chatbot:app --reload
Test API Endpoints

Send Prompt:
POST http://localhost:8000/prompt
Body:
{
  "text": "Your question here"
}
Add New Data:
POST http://localhost:8000/add_data
Body:
{
  "text": "New context or text to add"
}

Frontend (Streamlit)
Run the Streamlit Interface Start the testapp.py script to launch the chatbot interface:

streamlit run testapp.py
Interacting with the Chatbot

Enter your question in the text box.
Click Send to get a response from the chatbot.
The response will be displayed, and you can play the audio generated using UnrealSpeech.
Customization
Modify the Prompt Template: You can change the behavior of the chatbot by adjusting the prompt in chatbot.py. 
For example, modify how the context is presented or the chatbot's tone.

template = """
You are an AI-powered assistant. Please respond to the question based on the context below:
Context: {context}
Question: {question}
"""
Change the Text-to-Speech Settings: You can change the voice, speed, and other parameters in the text_to_speech function in testapp.py. Available voices include Dan, Will, Scarlett, etc.


'VoiceId': 'Scarlett', # Change to other voice options
'Speed': '0.2', # Adjust the speed of speech
Using Different Models: You can switch between OpenAI's GPT and ChatGroq models by changing the model in chatbot.py.

Dependencies
LangChain: For interacting with OpenAI models and managing vector embeddings.
OpenAI: For GPT-3.5 Turbo API.
FastAPI: For creating the backend API.
Streamlit: For building the frontend interface.
Pinecone: For vector search and document retrieval.
UnrealSpeech API: For converting text to speech.

To install the dependencies, run:
pip install -r requirements.txt

License
This project is licensed under the MIT License. You are free to use, modify, and distribute this project.

