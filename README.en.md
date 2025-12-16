# 📚 Chat API with AI Agent  
### ⭐ FastAPI + Strands Agents + Ollama (Model with Native Tool Use)

This project implements a **chat API** that uses the **Strands Agents SDK**, integrated with **Ollama**, to create an AI agent capable of:

- Answering general knowledge questions  
- Detecting when mathematical tools should be used  
- Automatically performing calculations using an **LLM with native tool-use** (`llama3-groq-tool-use`)  
- Conversing naturally with the user  

This project follows the best practices required in the case, with proper organization, environment variable usage, and a clear separation between the API and the AI agent.

---

# 🗂️ Project Structure
```
API_de_Chat_com_Agente_de_IA/
├── src/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   ├── main.py
│   ├── schemas.py
│
├── teste.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```
---

## 🔧 1. Environment Configuration

The project uses a `.env` file at the root to define its settings.

Create your `.env` file:

    cp .env.example .env

Default content:

    LLM_PROVIDER=ollama
    LLM_MODEL=llama3-groq-tool-use

    LLM_TEMPERATURE=0.2
    LLM_MAX_TOKENS=1024

    OLLAMA_HOST=http://localhost:11434

    APP_ENV=local

- `LLM_MODEL` points to the model that already has native tool-use  
- `OLLAMA_HOST` is the local Ollama server  
- `APP_ENV` indicates the runtime environment  

---

## 📦 2. Dependencies

The `requirements.txt` file contains:

    fastapi
    uvicorn[standard]
    strands-agents
    strands-agents-tools
    python-dotenv

Install dependencies:

    pip install -r requirements.txt

---

## 🤖 3. Agent Implementation (Strands Agents + Ollama)

The `src/agent.py` file contains the full implementation of the AI agent responsible for interpreting the user message and generating the final response using Strands Agents and Ollama.

### ✔️ Ollama Model Loading

The agent uses `OllamaModel`, configured through variables defined in the `.env` file:

- `LLM_MODEL`
- `LLM_TEMPERATURE`
- `LLM_MAX_TOKENS`
- `OLLAMA_HOST`

This allows the model behavior to be adjusted without changing the code.

### ✔️ Native Tool Use

The project uses the **`llama3-groq-tool-use`** model, which already includes native support for tool use:

- Mathematical calculations  
- Structured reasoning  
- Automatic tool selection  
- Intelligent command interpretation  

No tools were manually implemented in Python.  
The model itself decides when to use a tool or respond directly.

### ✔️ System Prompt

The agent includes a *system prompt* that guides the model’s behavior:

- When to use tool-use  
- How to answer general questions  
- Language consistency  
- Maintaining coherence  

### ✔️ run_agent(message)

This function:

1. Receives the user message  
2. Sends it to the Strands agent  
3. Processes the request via Ollama  
4. Returns the final response as a string  

It centralizes agent execution and simplifies reuse.

---

## 🌐 4. FastAPI API (src/main.py)

### POST /chat

Input:

    {
      "message": "What is 1234 * 5678?"
    }

Output:

    {
      "response": "7006652"
    }

### GET /health

Response:

    {
      "status": "ok"
    }

---

## 🧠 5. Ollama Integration

### Installation

    curl -fsSL https://ollama.com/install.sh | sh

Verify:

    ollama -v

### Download Model

    ollama pull llama3-groq-tool-use

### Start Server

    ollama serve

---

## ▶️ How to Run

Start API:

    uvicorn src.main:app --reload

Docs:

    http://127.0.0.1:8000/docs

---

## 🧪 6. Tests and Validation

### Agent Test

    python teste.py

### Swagger

    http://localhost:8000/docs

### cURL Example

    curl -X POST http://localhost:8000/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "What is 55 * 99?"}'

---

## 🎉 Completed Phases

- ✔️ Phase 1 — Structure  
- ✔️ Phase 2 — Configuration  
- ✔️ Phase 3 — Dependencies  
- ✔️ Phase 4 — FastAPI API  
- ✔️ Phase 5 — Ollama Integration  
- ✔️ Phase 6 — Tests and Validation  

---

## 🏁 Project Conclusion

This project delivers a fully functional Chat API integrated with an AI Agent using FastAPI, Strands Agents, and the local `llama3-groq-tool-use` model via Ollama.

It demonstrates:

- Clean architecture  
- Proper use of environment variables  
- Native tool-use with LLMs  
- API validation via multiple methods  

The solution is complete, validated, and ready for technical evaluation.
