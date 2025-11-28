#%%

import os
import sys
sys.path.append(os.path.abspath(".."))
from src.config import settings

from strands.agent import Agent
from strands.tools import tool
from strands.models.ollama import OllamaModel
strands.tool = tool
from strands_tools import calculator

from src.agent import run_agent


print(settings.LLM_PROVIDER, settings.LLM_MODEL, settings.APP_ENV)

# %%

from src.agent import run_agent

print(run_agent("Quanto é 1234 * 5678?"))
print(run_agent("Qual a raiz quadrada de 144?"))
print(run_agent("Quem foi Albert Einstein?"))

# %%
