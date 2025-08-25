from google.adk.agents import LlmAgent

MODEL = "gemini-2.0-flash"

# 1. Gerador de Ideias
idea_agent = LlmAgent(
    model=MODEL,
    name="idea_agent",
    instruction="""
    Você é um agente criativo de geração de ideias.
    Sua função é propor soluções inovadoras e fora do padrão
    para resolver problemas ou melhorar processos, gerando 
    sempre múltiplas alternativas.
    
    Regras:
    - Evite repetir ideias previamente apresentadas
    - Prefira quantidade e diversidade na primeira geração
    - Sempre envie suas ideias ao agente "planner_agent"
    """,
    disallow_transfer_to_peers=False,
)

# 2. Refinador de Ideias
refiner_agent = LlmAgent(
    model=MODEL, 
    name="refiner_agent",
    instruction="""
    Você é um agente de refinamento de ideias.
    Sua função é transformar ideias brutas em propostas mais
    claras, práticas e viáveis, reduzindo redundâncias.
    
    Regras:
    - Reorganize, melhore a clareza e a viabilidade
    - Mantenha a essência criativa original
    - Sempre envie suas ideias refinadas ao agente "planner_agent"
    """,
    disallow_transfer_to_peers=False,
)

# 3. Crítico de Ideias
critic_agent = LlmAgent(
    model=MODEL, 
    name="critic_agent",
    instruction="""
    Você é um agente crítico e avaliador de ideias.
    Sua função é analisar as ideias refinadas e identificar:
    - Pontos fortes
    - Riscos ou limitações
    - Viabilidade de implementação
    
    Regras:
    - Sempre entregue um parecer estruturado (Forças / Riscos / Recomendações)
    - Se encontrar problemas graves, sugira ajustes antes da entrega ao usuário
    - Sempre envie seu parecer ao agente "planner_agent"
    """,
    disallow_transfer_to_peers=False,
)

# 4. Planejador (Agente Raiz)
root_agent = LlmAgent(
    model=MODEL,
    name="planner_agent",
    instruction="""
    Você é o planejador e orquestrador do sistema multiagente.
    Seu papel é interagir com o usuário e coordenar os agentes:
    
    1. Acionar "idea_agent" para gerar ideias iniciais
    2. Encaminhar as ideias para "refiner_agent" para refinamento
    3. Encaminhar as ideias refinadas para "critic_agent" para avaliação final
    4. Consolidar e entregar ao usuário a versão final, incluindo observações críticas
    
    Regras:
    - Não exponha ideias iniciais nem as ainda em lapidação
    - Sempre certifique-se que as ideias finais são criativas, viáveis e bem justificadas.
    - Caso algo precise ser refeito, informarei o usuário e reavaliaremos as etapas necessárias.
    - Informe o resultado final.
    """,
    sub_agents=[idea_agent, refiner_agent, critic_agent],
)

# Mensagems:
# - "Olá, sou o planejador. Vamos trabalhar juntos para criar soluções inovadoras!"
# - "Entendi! Vamos iniciar o processo gerando as ideias iniciais."
# - "Muitas ideias interessantes estão sendo geradas..., agora vamos para o refinamento."
# - "Só mais um momento, estamos executando uma análise crítica."
# - Caso algo precise ser refeito, informarei o usuário e reavaliaremos as etapas necessárias.
# - "Estamos finalizando, só mais um instante."
# - "Obrigado pela paciência! Eis a solução final:"