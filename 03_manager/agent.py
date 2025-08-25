from google.adk.agents import Agent

# from .sub_agents.idea_agent.agent import idea_agent
# from .sub_agents.refiner_agent.agent import refiner_agent
# from .sub_agents.critic_agent.agent import critic_agent

from .sub_agents import idea_agent, critic_agent, refiner_agent
from .config import MODEL

root_agent = Agent(
    name="manager",
    model=MODEL,
    description="Manager Agent",
    instruction="""
    Você é o Manager Agent. 
    Seu papel é atuar como um agente cognitivo, que interage diretamente com o usuário
    e decide como processar cada solicitação.

    - Se a solicitação for simples e direta (ex.: perguntas objetivas como horário ou clima),
      responda imediatamente sem acionar os demais agentes.
    - Se a solicitação exigir criatividade, planejamento ou revisão,
      siga o fluxo hierárquico:

      1. Enviar para o `idea_agent` gerar ideias.
      2. Enviar para o `refiner_agent` melhorar e tornar as ideias práticas.
      3. Enviar para o `critic_agent` revisar e gerar o resultado final.

    - Sempre retorne apenas o resultado final ao usuário.
    """,
    sub_agents=[idea_agent, refiner_agent, critic_agent],  # cadeia de agentes operacionais
    disallow_transfer_to_peers=True,
)
