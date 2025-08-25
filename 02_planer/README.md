# Agente Planejador (02_planer)

Este agente utiliza um padrão de equipe de agentes para criar um plano detalhado a partir de um objetivo fornecido pelo usuário. Ele orquestra um fluxo de trabalho entre três sub-agentes especializados para gerar, criticar e refinar ideias.

## Funcionalidade e Estrutura

O agente planejador funciona orquestrando sub-agentes, cada um com uma responsabilidade específica. A estrutura de arquivos reflete essa organização:

```
02_planer/
├── agent.py           # Agente orquestrador principal
└── sub_agents/
    ├── idea_agent.py    # Sub-agente que gera ideias
    ├── critic_agent.py  # Sub-agente que avalia as ideias
    └── refiner_agent.py # Sub-agente que refina o plano final
```

O fluxo é o seguinte:
1.  O `agent.py` principal recebe a solicitação.
2.  Ele a repassa para o `idea_agent` para gerar as etapas iniciais.
3.  As ideias são enviadas ao `critic_agent` para avaliação.
4.  Finalmente, o `refiner_agent` consolida as informações para criar o plano final.

## Como Executar

Para interagir com este agente, você deve executar:

```powershell
adk web
```

Após a execução, uma URL será disponibilizada no terminal para que você possa acessar a interface dos agentes em seu navegador.
