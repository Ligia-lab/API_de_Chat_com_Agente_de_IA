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
    """
    Função principal de execução para testes locais do agente de IA.

    Esta função é utilizada como um script de validação e demonstração do funcionamento
    do agente fora do contexto da API. Ela exibe as configurações carregadas a partir das
    variáveis de ambiente e executa uma série de perguntas de exemplo para verificar o
    comportamento do agente em diferentes cenários.

    O fluxo da função consiste em:
    1. Exibir no terminal as configurações principais do LLM e do ambiente da aplicação.
    2. Definir um conjunto de perguntas que incluem tanto cálculos matemáticos quanto
       perguntas de conhecimento geral.
    3. Iterar sobre as perguntas, enviando cada uma ao agente por meio da função
       `run_agent()`.
    4. Exibir a resposta gerada pelo agente ou, em caso de erro, imprimir o traceback
       para facilitar o diagnóstico durante o desenvolvimento.

    Essa função é especialmente útil para testes rápidos, debug e validação do uso de
    ferramentas pelo agente, sem a necessidade de subir o servidor FastAPI.
    """
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
