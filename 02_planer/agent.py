from google.adk.agents import LlmAgent

from .sub_agents.idea_agent import idea_agent
from .sub_agents.refiner_agent import refiner_agent
from .sub_agents.critic_agent import critic_agent
from .sub_agents.config import MODEL

root_agent = LlmAgent(
    name="planer",
    model=MODEL,
    description="Planner Agent",
    instruction="""
    Você é o Planner Agent. 
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
)
