from google.adk.agents import Agent

critic_agent = Agent(
    name="critic_agent",
    description="Agente responsável por revisar e refinar o conteúdo gerado por outros agentes.",
    instruction="""
    Você é o Critic Agent.
    Sua função é revisar o conteúdo refinado, identificar erros, incoerências ou 
    oportunidades de melhoria, e entregar a versão final pronta para o usuário.
    """,
    disallow_transfer_to_peers=False,
)
