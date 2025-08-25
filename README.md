# Projeto de Treinamento com Multiagentes e Google ADK

## Objetivo

Este repositório é um projeto de treinamento focado no desenvolvimento de sistemas multiagentes utilizando o **Google Agent Development Kit (ADK)**. O objetivo é explorar diferentes padrões de arquitetura, desde agentes simples até sistemas mais complexos com orquestração e estruturas de projeto escaláveis.

## Estrutura do Projeto

A estrutura do workspace foi montada para simplificar a usabilidade e o desenvolvimento dos agentes, compartilhando um único ambiente virtual (`.venv`) e uma configuração de projeto centralizada (`pyproject.toml`).

Cada agente ou padrão de arquitetura está contido em seu próprio diretório numerado.

### Agentes Implementados (até 25 de agosto de 2025)

-   **`01_agent_adk/`**: Um agente simples e fundamental que serve como ponto de partida. Ele recebe uma instrução e a responde diretamente, demonstrando os conceitos básicos do ADK.
-   **`02_planer/`**: Um agente planejador que decompõe um objetivo em passos menores. Ele utiliza sub-agentes para gerar ideias, criticá-las e refiná-las, criando um plano de ação coeso.
-   **`03_manager/`**: Um agente gerente que implementa a mesma lógica do planejador, mas com uma estrutura de diretórios mais robusta e modular, alinhada com as melhores práticas de desenvolvimento de software.

## Pré-requisitos

-   Python 3.12+
-   [UV](https://github.com/astral-sh/uv) (uma ferramenta de instalação e gerenciamento de pacotes Python)

## Como Começar

### 1. Baixar ou Clonar o Repositório

Primeiro, obtenha os arquivos do projeto em sua máquina local.

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
```

### 2. Configurar o Ambiente

Depois de baixar o projeto, você precisa recriar o ambiente virtual e instalar as dependências.

**a. Inicialize o projeto com UV**

Se o arquivo `pyproject.toml` já existir, sincronize as dependências para instalar o que está definido nele:
```powershell
uv sync
```
Caso contrário, você pode inicializar um novo projeto (isso criará um `pyproject.toml`):
```powershell
uv init
```

**b. Crie e ative o ambiente virtual**

```powershell
# Criar o ambiente
uv venv .venv

# Ativar no Windows (PowerShell/CMD)
.venv\Scripts\Activate

# Ativar no Linux/macOS (Bash/Zsh)
source .venv/bin/activate
```

**c. Instale os pacotes básicos**

```powershell
uv add google-adk google-generativeai python-dotenv
```

> **Atenção para usuários do OneDrive:** Se o seu projeto está em um diretório sincronizado com o OneDrive, use o seguinte comando para evitar problemas de links simbólicos:
>
> ```powershell
> uv add --link-mode=copy google-adk google-generativeai python-dotenv
> ```

## Configuração da API Key

**Antes de executar os agentes, é fundamental configurar sua chave de API do Google.**

1.  **Crie um arquivo `.env`** na raiz do projeto, caso ele não exista.
2.  **Adicione a seguinte linha** ao arquivo `.env`:
    ```
    GOOGLE_API_KEY="SUA_CHAVE_API_AQUI"
    ```
3.  **Substitua `"SUA_CHAVE_API_AQUI"`** pela sua chave de API.

### Como Obter uma Chave de API de Teste

Você pode obter uma chave de API gratuita para testes no **Google AI Studio**:

1.  Acesse o [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Faça login com sua conta do Google.
3.  Clique em **"Create API key"** para gerar uma nova chave.
4.  Copie a chave gerada e cole-a no seu arquivo `.env`.

## Como Executar os Agentes

Para interagir com os agentes, você deve executar:

```powershell
adk web
```

Após a execução, uma URL será disponibilizada no terminal para que você possa acessar a interface dos agentes em seu navegador.

---

## Desenvolvido por
**Marcel Quintela**
-   **LinkedIn:** [https://www.linkedin.com/in/marcelquintela/](https://www.linkedin.com/in/marcelquintela/)
-   **GitHub:** [https://github.com/Marcelquintela](https://github.com/Marcelquintela)
```