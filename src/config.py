#%%

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """
    Classe responsável por centralizar e gerenciar as configurações da aplicação.

    Esta classe lê as variáveis de ambiente necessárias para o funcionamento do sistema,
    especialmente aquelas relacionadas ao uso do modelo de linguagem (LLM) e ao ambiente
    de execução da aplicação. As variáveis são carregadas automaticamente a partir de um
    arquivo `.env` (quando disponível), utilizando a biblioteca `python-dotenv`.

    As principais configurações incluem:
    - `LLM_PROVIDER`: define o provedor do modelo de linguagem (ex.: Ollama).
    - `LLM_MODEL`: especifica qual modelo LLM será utilizado.
    - `LLM_TEMPERATURE`: controla o nível de criatividade das respostas do modelo.
    - `LLM_MAX_TOKENS`: limita o número máximo de tokens gerados por resposta.
    - `APP_ENV`: identifica o ambiente de execução (local, desenvolvimento, produção).

    Após carregar as variáveis, a classe executa uma validação básica para garantir que
    as configurações essenciais estejam definidas, evitando falhas silenciosas em tempo
    de execução.

    A instância `settings` é criada de forma global e pode ser reutilizada em toda a
    aplicação, garantindo consistência e centralização das configurações.
    """
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
