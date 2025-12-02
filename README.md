# 📚 API de Chat com Agente de IA  
### ⭐ FastAPI + Strands Agents + Ollama (modelo com Tool Use nativo)

Este projeto implementa uma **API de chat** que utiliza o **Strands Agents SDK**, integrado com o **Ollama**, para criar um agente de IA capaz de:

- Responder perguntas de conhecimento geral  
- Detectar quando deve usar ferramentas matemáticas  
- Realizar cálculos automaticamente usando **LLM com tool-use nativo** (`llama3-groq-tool-use`)  
- Conversar naturalmente com o usuário  

Esse projeto segue as boas práticas solicitadas no case, com organização, uso de variáveis de ambiente e separação clara entre API e Agente de IA.

---

# 🗂️ Estrutura do Projeto


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

## 🔧 1. Configuração do Ambiente

O projeto utiliza um arquivo `.env` na raiz para definir suas configurações.

Crie seu `.env`:

```bash
cp .env.example .env
```

O conteúdo padrão:
```
LLM_PROVIDER=ollama
LLM_MODEL=llama3-groq-tool-use

LLM_TEMPERATURE=0.2
LLM_MAX_TOKENS=1024

OLLAMA_HOST=http://localhost:11434

APP_ENV=local
```

LLM_MODEL aponta para o modelo que já possui tool-use nativo

OLLAMA_HOST é o servidor local do Ollama

APP_ENV indica ambiente de execução

---

## 📦 2. Dependências

O arquivo `requirements.txt` contém:

```
fastapi
uvicorn[standard]
strands-agents
strands-agents-tools
python-dotenv
```

Instalação das dependências:

```bash
pip install -r requirements.txt
```
---
## 🤖 3. Implementação do Agente (Strands Agents + Ollama)

O arquivo `src/agent.py` contém toda a implementação do agente de IA responsável por interpretar a mensagem do usuário e gerar a resposta final utilizando o Strands Agents e o Ollama.

### ✔️ Carregamento do modelo Ollama

O agente utiliza o `OllamaModel`, configurado através das variáveis definidas no arquivo `.env`.  
Essas configurações incluem:

- `LLM_MODEL`: nome do modelo  
- `LLM_TEMPERATURE`: temperatura do modelo  
- `LLM_MAX_TOKENS`: máximo de tokens de resposta  
- `OLLAMA_HOST`: endereço do servidor Ollama  

Isso permite que o comportamento do modelo seja facilmente ajustado sem alterar o código.

### ✔️ Tool-Use nativo do modelo

O projeto utiliza o modelo **`llama3-groq-tool-use`**, que já possui suporte nativo para tool-use, incluindo:

- execução de cálculos matemáticos  
- raciocínio estruturado  
- seleção automática de ferramentas internas  
- interpretação inteligente de comandos  

Nenhuma tool foi implementada manualmente no Python.  
O próprio modelo decide quando usar uma ferramenta ou quando responder diretamente.

### ✔️ System Prompt

O agente possui um *system prompt* que orienta o modelo quanto ao comportamento esperado, incluindo:

- quando usar tool-use  
- como responder perguntas gerais  
- como manter coerência e linguagem adequada  
- manter o idioma da resposta igual ao input do usuário  

Esse prompt garante consistência nas respostas e melhora a qualidade da interação.

### ✔️ Função `run_agent(message)`

A função `run_agent` é utilizada tanto pela API quanto pelo arquivo `teste.py`.  
Ela executa o fluxo:

1. Recebe a mensagem do usuário  
2. Envia essa mensagem ao agente Strands  
3. Aguarda o processamento do modelo via Ollama  
4. Retorna a resposta final formatada como string  

Essa função centraliza a execução do modelo e facilita a reutilização do agente em várias partes do projeto.

---

## 🌐 4. API FastAPI (src/main.py)

A API expõe dois endpoints:

### POST /chat

**Entrada:**

    {
      "message": "Quanto é 1234 * 5678?"
    }

**Saída:**

    {
      "response": "7006652"
    }

### GET /health

**Resposta:**

    {
      "status": "ok"
    }

---

## 🧠 5. Integração com o Ollama

Este projeto usa o **Ollama** para rodar o modelo localmente.

### 5.1 Instalação

    curl -fsSL https://ollama.com/install.sh | sh

Verifique a instalação:

    ollama -v

### 5.2 Baixar o modelo requerido

    ollama pull llama3-groq-tool-use

Listar modelos:

    ollama list

### 5.3 Servidor do Ollama

Inicie o servidor do Ollama:

    ollama serve

---

## ▶️ Como Rodar

Subir a API FastAPI:

    uvicorn src.main:app --reload

Documentação:

    http://127.0.0.1:8000/docs

---

## 🧪 Testando o Agente

Executar o script de teste:

    python teste.py
---
## 🧪 6. Testes e Validação

Esta fase garante que o agente, a API e a integração com o Ollama estão funcionando corretamente.

---

### 6.1 Testando o Agente diretamente (teste.py)

Execute:

    python teste.py

Resultados esperados:

- Pergunta matemática:
    Input:
        Quanto é 1234 * 5678?
    Output esperado:
        7006652

- Raiz quadrada:
    Input:
        Qual a raiz quadrada de 144?
    Output esperado:
        12

- Pergunta geral:
    Input:
        Quem foi Ada Lovelace?
    Output esperado:
        Uma explicação descritiva.

---

### 6.2 Testando a API via Swagger

Acesse:

    http://localhost:8000/docs

Teste o endpoint POST /chat:

Entrada:

    {
      "message": "Qual a raiz quadrada de 144?"
    }

Saída esperada:

    {
      "response": "12"
    }

Teste pergunta geral:

Entrada:

    {
      "message": "Explique o que é machine learning."
    }

---

### 6.3 Testando via cURL

Teste de cálculo:

    curl -X POST http://localhost:8000/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "Quanto é 55 * 99?"}'

Teste pergunta geral:

    curl -X POST http://localhost:8000/chat \
    -H "Content-Type: application/json" \
    -d '{"message": "Quem inventou o avião?"}'

---

### 6.4 Verificando o Ollama

Listar modelos:

    ollama list

Testar diretamente o modelo:

    ollama run llama3-groq-tool-use "Quanto é 120 * 88?"

---

### 6.5 Casos de teste recomendados (tool-use)

    Quanto é 8 ** 3?
    Raiz quadrada de 256.
    Calcule 55 * 45.
    Quanto é 0.55 * 1200?

---

### 6.6 Casos de teste recomendados (conhecimento geral)

    Quem foi Albert Einstein?
    Explique redes neurais.
    O que é Python?
    Explique o conceito de API.

---

### 6.7 Resultado da Fase 6

- O agente resolve cálculos corretamente.  
- O agente responde perguntas gerais de forma coerente.  
- O endpoint POST /chat funciona via Swagger e cURL.  
- O modelo llama3-groq-tool-use está operando corretamente no Ollama.  
- Toda a aplicação está validada e funcional.



---

## 🎉 Fases concluídas

- ✔️ Fase 1 — Estrutura  
- ✔️ Fase 2 — Configuração  
- ✔️ Fase 3 — Dependências  
- ✔️ Fase 4 — API FastAPI  
- ✔️ Fase 5 — Integração com Ollama
- ✔️ Fase 6 — Testes e Validação


---

