# Chat API with AI Agent

A simple **chat API** built with **FastAPI** and an **AI agent** that uses the **Strands Agents SDK** and **Ollama** as the language model.  
This project demonstrates how to build a structured LLM-driven API with tool usage, clean architecture, and environment-based configuration.

---

## 🚀 Features

- Conversational AI API using FastAPI
- AI Agent with tool support (calculator for math operations)
- Local LLM inference using Ollama
- Clean and extensible architecture
- Typed request and response schemas with Pydantic
- Local testing without running the API server

---

## 📋 Project Structure

API_de_Chat_com_Agente_de_IA/
- src/
  - agent.py        → AI agent creation and execution logic
  - config.py       → Environment-based application settings
  - schemas.py      → API request and response models
  - main.py         → FastAPI application and endpoints
- teste.py          → Local test script for the agent
- README.md
- requirements.txt

---

## ⚙️ Configuration

Create a `.env` file in the project root with the following variables:

LLM_PROVIDER=ollama  
LLM_MODEL=llama3  
LLM_TEMPERATURE=0.2  
LLM_MAX_TOKENS=1024  
APP_ENV=local  
OLLAMA_HOST=http://localhost:11434  

These variables define the LLM provider and model, inference parameters,
the application environment, and the Ollama server address.

---

## 🧠 AI Agent Design

The core logic lives in `agent.py`. The agent:

1. Initializes the LLM through a dedicated model factory function  
2. Registers tools (such as a calculator for math operations)  
3. Uses a system prompt to control behavior and tool usage  
4. Executes requests through a single interface function  

A lazy-loaded singleton pattern ensures the agent is created only once,
improving performance and resource usage.

---

## 📡 API Endpoints

### POST /chat

Send a user message to the AI agent.

Request example:
{ "message": "What is machine learning?" }

Response example:
{ "response": "Machine learning is a field of AI that allows systems to learn from data." }

---

### GET /health

Health-check endpoint.

Response:
{ "status": "ok" }

---

## 🧪 Local Testing (Without API)

You can test the agent directly using the provided script:

python teste.py

This script prints the loaded configuration values and sends multiple
example questions to the agent, validating both tool usage and general
conversational responses.

---

## 🛠️ Installation & Running

Clone the repository:

git clone https://github.com/Ligia-lab/API_de_Chat_com_Agente_de_IA.git  
cd API_de_Chat_com_Agente_de_IA  

Create and activate a virtual environment:

python3 -m venv venv  
source venv/bin/activate  

Install dependencies:

pip install -r requirements.txt  

Start the API server:

uvicorn src.main:app --reload  

---

## 📖 API Documentation

Once running, access Swagger UI at:

http://localhost:8000/docs

---

## 🔍 Example Use Cases

- Math questions (tool invocation):  
  How much is 1234 * 5678?

- General knowledge questions:  
  Who was Ada Lovelace?

- Technical explanations:  
  Explain machine learning in simple terms.

---

## 📈 Project Highlights

- Demonstrates LLM agent architecture
- Shows practical tool usage with AI agents
- Environment-driven configuration
- Local LLM inference without external APIs
- Interview-ready example of AI system design

---

## 🚧 Future Improvements

- Add conversation memory
- Support more tools (search, database, APIs)
- Authentication and rate limiting
- Logging and monitoring
- Docker and production deployment

---

## 📜 License

This project is open-source and free to use for learning and experimentation.
