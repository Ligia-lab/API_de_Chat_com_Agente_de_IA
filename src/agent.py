#%% 
import sys
import os

sys.path.append(os.path.abspath(".."))

from strands.agent import Agent
from strands.tools import tool
from strands.models.ollama import OllamaModel
#strands.tool = tool
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

#%%

def _create_model() -> OllamaModel:
    """
    Cria e configura a instância do modelo de linguagem (LLM) utilizado pelo agente de IA.

    Esta função é responsável por inicializar um modelo do Ollama, lendo as configurações
    a partir de variáveis de ambiente e do objeto `settings`. O endereço do servidor Ollama
    pode ser configurado via a variável de ambiente `OLLAMA_HOST`, permitindo flexibilidade
    entre ambientes (local, container ou servidor). Caso não seja informado, utiliza o
    valor padrão `http://localhost:11434`.

    O modelo é configurado com parâmetros importantes de inferência, como:
    - `model_id`: identifica qual modelo LLM será utilizado (ex.: llama3).
    - `temperature`: controla o nível de criatividade das respostas.
    - `max_tokens`: limita o tamanho máximo da resposta gerada.

    Ao encapsular a criação do modelo em uma função dedicada, o código fica mais organizado,
    reutilizável e facilita futuras mudanças de configuração ou troca do provedor de LLM.

    Returns:
        OllamaModel: instância do modelo de linguagem pronta para ser usada pelo agente.
    """
   
    ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434") #padrão ollama

    model = OllamaModel(
        host=ollama_host,
        model_id=settings.LLM_MODEL,
        temperature=settings.LLM_TEMPERATURE,
        max_tokens=settings.LLM_MAX_TOKENS,
    )
    return model

#%%

def _create_agent() -> Agent:
    """
    Cria e configura a instância do agente de IA responsável por processar as mensagens do usuário.

    Esta função inicializa um agente utilizando a abstração de `Agent` da biblioteca Strands,
    associando a ele um modelo de linguagem previamente configurado e um conjunto de ferramentas
    auxiliares. O modelo é obtido por meio da função `_create_model()`, garantindo separação
    de responsabilidades entre a criação do LLM e a lógica do agente.

    O agente é configurado com:
    - `model`: o modelo de linguagem (LLM) que gera as respostas.
    - `tools`: uma lista de ferramentas que o agente pode acionar durante a execução. Neste
      projeto, a ferramenta `calculator` é utilizada para resolver cálculos matemáticos de
      forma explícita e confiável.
    - `system_prompt`: um prompt de sistema que define o comportamento do agente, orientando
      quando ele deve responder diretamente e quando deve delegar cálculos para a ferramenta.

    Essa abordagem segue o padrão de agentes com ferramentas (tool-using agents), permitindo
    que o LLM tome decisões e execute ações de forma controlada, tornando as respostas mais
    seguras, precisas e determinísticas.

    Returns:
        Agent: instância do agente de IA pronta para receber mensagens do usuário.
    """
 
    model = _create_model()

    agent = Agent(
        model=model,
        tools=[calculator],      #cálculo matemático
        system_prompt=SYSTEM_PROMPT,
    )

    return agent

#%%

_agent_instance: Agent | None = None

def get_agent() -> Agent:
    """
    Retorna a instância única do agente de IA utilizada pela aplicação.

    Esta função implementa um padrão de inicialização tardia (lazy initialization)
    combinado com um comportamento semelhante a Singleton, garantindo que apenas
    uma instância do agente seja criada e reutilizada durante todo o ciclo de vida
    da aplicação.

    Caso o agente ainda não exista, a função chama `_create_agent()` para criá-lo.
    Nas chamadas subsequentes, a instância já existente é reutilizada, evitando
    custos desnecessários de reconfiguração do modelo de linguagem e das ferramentas
    associadas.

    Essa abordagem melhora a performance da aplicação, reduz o tempo de resposta
    e centraliza o gerenciamento do agente, especialmente em cenários de APIs
    que lidam com múltiplas requisições.

    Returns:
        Agent: instância única do agente de IA.
    """
  
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = _create_agent()
    return _agent_instance

#%%

def run_agent(message: str) -> str:
    """
    Executa o agente de IA para processar uma mensagem e retorna a resposta gerada.

    Esta função é a interface principal utilizada para interagir com o agente de IA.
    Ela recebe uma mensagem do usuário como entrada, chama o agente para processar
    a mensagem e retorna a resposta gerada. O agente pode utilizar tanto o modelo
    de linguagem quanto ferramentas auxiliares (como a ferramenta `calculator`) para
    fornecer uma resposta precisa e controlada.

    O processo inclui:
    1. Obtenção da instância única do agente via `get_agent()`.
    2. Execução do agente com a mensagem fornecida.
    3. Verificação de se a resposta contém um atributo `final_response` (usado
       quando o agente faz múltiplos passos ou cálculos) e retorno da resposta.
    4. Caso contrário, retorna a resposta diretamente do agente.

    Isso permite que o agente lide com diferentes tipos de mensagens (como perguntas
    gerais ou cálculos matemáticos) de forma flexível e consistente.

    Args:
        message (str): A mensagem do usuário que será processada pelo agente de IA.

    Returns:
        str: A resposta gerada pelo agente, seja um texto direto ou o resultado final
             de uma ferramenta utilizada pelo agente.
    """

    agent = get_agent()
    result = agent(message)

    if hasattr(result, "final_response"):
        return str(result.final_response)

    return str(result)

# %%

