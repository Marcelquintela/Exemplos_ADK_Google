# Agente Gerente (03_manager)

Este agente executa a mesma função de planejamento que o `02_planer`, mas adota uma estrutura de diretórios mais robusta e escalável, alinhada com as melhores práticas de desenvolvimento de software.

## Funcionalidade e Estrutura

A lógica de orquestração entre os agentes de ideação, crítica e refinamento é a mesma do agente planejador (`02_planer`). A principal diferença e melhoria está na organização dos arquivos, que promove maior modularidade e manutenibilidade.

Cada sub-agente agora reside em seu próprio diretório, tornando o projeto mais fácil de navegar e escalar:

```
03_manager/
├── agent.py             # Agente orquestrador principal (Gerente)
├── config/              # Diretório para configurações
├── sub_agents/
│   ├── idea_agent/
│   │   └── agent.py     # Módulo do sub-agente de ideias
│   ├── critic_agent/
│   │   └── agent.py     # Módulo do sub-agente crítico
│   └── refiner_agent/
│       └── agent.py     # Módulo do sub-agente refinador
└── tools/                 # Diretório para ferramentas (ex: APIs, funções)
```

Esta abordagem é considerada uma prática recomendada porque isola as responsabilidades, facilitando a manutenção e a reutilização de cada componente.

## Como Executar

Para interagir com este agente, você deve executar:

```powershell
adk web
```

Após a execução, uma URL será disponibilizada no terminal para que você possa acessar a interface dos agentes em seu navegador.
