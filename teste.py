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

import traceback

from src.config import settings
from src.agent import run_agent


def main():
    print("=== Settings carregados ===")
    print("LLM_PROVIDER:", settings.LLM_PROVIDER)
    print("LLM_MODEL:", settings.LLM_MODEL)
    print("APP_ENV:", settings.APP_ENV)
    print()

    perguntas = [
        "Quanto é 1234 * 5678?",
        "Quem é Valentino Rossi?",
        "Quem foi Ada Lovelace?",
        "Explique de forma simples o que é machine learning.",
    ]

    for pergunta in perguntas:
        print(f">>> Usuário: {pergunta}")
        try:
            resposta = run_agent(pergunta)
            print(f"Agente: {resposta}")
        except Exception:
            print("❌ Erro ao chamar o agente. Traceback:")
            traceback.print_exc()
            break

        print("-" * 70)


if __name__ == "__main__":
    main()

# %%
