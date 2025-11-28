#%%

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        
        self.LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")
        self.LLM_MODEL = os.getenv("LLM_MODEL", "llama3")

        self.LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", 0.2))
        self.LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", 1024))

        self.APP_ENV = os.getenv("APP_ENV", "local")

        self._validate()

    def _validate(self):
        """Valida se as variáveis essenciais foram definidas."""
        if not self.LLM_PROVIDER:
            raise ValueError("A variável de ambiente LLM_PROVIDER não foi definida.")
        if not self.LLM_MODEL:
            raise ValueError("A variável de ambiente LLM_MODEL não foi definida.")

settings = Settings()

# %%
