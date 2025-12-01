#%%

import sys
import os

sys.path.append(os.path.abspath(".."))

#%%

from strands.agent import Agent
from strands.tools import tool
from strands.models.ollama import OllamaModel
from strands_tools import calculator
from src.config import settings
from src.agent import run_agent

print(settings.LLM_PROVIDER, settings.LLM_MODEL, settings.APP_ENV)

# %%
