#%% 
import sys
import os

sys.path.append(os.path.abspath(".."))

from strands.agent import Agent
from strands.tools import tool
from strands.models.ollama import OllamaModel
strands.tool = tool
from strands_tools import calculator

from src.config import settings
import os

# %%

SYSTEM_PROMPT = """
You are a helpful chat assistant that can both talk naturally and solve math problems.

- When the user asks for any non-trivial calculation (multiplication, division, powers, roots,
  percentages, etc.), or explicitly asks something like "quanto é", "calculate", "raiz quadrada",
  you MUST use the `calculator` tool instead of doing the math yourself.
- For general knowledge questions that do not require calculations, answer directly without tools.
- Always return a concise answer in the same language as the user.
"""

# %%

def _create_model() -> OllamaModel:
   
    ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434") #padrão ollama

    model = OllamaModel(
        host=ollama_host,
        model_id=settings.LLM_MODEL,
        temperature=settings.LLM_TEMPERATURE,
        max_tokens=settings.LLM_MAX_TOKENS,
    )
    return model

# %%

def _create_agent() -> Agent:
 
    model = _create_model()

    agent = Agent(
        model=model,
        tools=[calculator],      #cálculo matemático
        system_prompt=SYSTEM_PROMPT,
    )

    return agent

# %%

_agent_instance: Agent | None = None

def get_agent() -> Agent:
  
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = _create_agent()
    return _agent_instance

# %%

def run_agent(message: str) -> str:

    agent = get_agent()
    result = agent(message)

    if hasattr(result, "final_response"):
        return str(result.final_response)

    return str(result)

# %%

