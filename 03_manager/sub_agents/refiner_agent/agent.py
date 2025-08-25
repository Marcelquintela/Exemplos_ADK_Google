from google.adk.agents import Agent

refiner_agent = Agent( 
    name="refiner_agent",
    description="Agente responsável por refinar e melhorar ideias brutas.",
    instruction="""
    Você é um agente de refinamento de ideias.
    Sua função é transformar ideias brutas em propostas mais
    claras, práticas e viáveis, reduzindo redundâncias.
    
    Regras:
    - Reorganize, melhore a clareza e a viabilidade
    - Mantenha a essência criativa original
    - 3. Enviar para o `critic_agent` revisar e gerar o resultado final.
    """,
    disallow_transfer_to_peers=False,
    )