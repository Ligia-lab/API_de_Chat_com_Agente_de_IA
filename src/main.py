#%%

import sys
import os

sys.path.append(os.path.abspath(".."))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src.schemas import ChatRequest, ChatResponse
from src.agent import run_agent

#%%

app = FastAPI(
    title="Chat API com Agente de IA",
    description="API simples de chat usando Strands Agents e Ollama como LLM.",
    version="1.0.0",
)

# (Opcional) habilitar CORS se quiser testar via frontend ou outro domínio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção, restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#%%

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest) -> ChatResponse:
    """
    Endpoint principal de chat.

    Recebe uma mensagem de texto do usuário e retorna
    a resposta do agente de IA.
    """
    if not payload.message or not payload.message.strip():
        raise HTTPException(status_code=400, detail="Campo 'message' não pode ser vazio.")

    try:
        resposta = run_agent(payload.message)
    except Exception as e:
        # Aqui você pode logar o erro de forma mais sofisticada se quiser
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar a mensagem: {e}",
        )

    return ChatResponse(response=resposta)

#%%

@app.get("/health")
async def health_check():
    """
    Endpoint simples de healthcheck, só pra verificar se a API está no ar.
    """
    return {"status": "ok"}

# %%
