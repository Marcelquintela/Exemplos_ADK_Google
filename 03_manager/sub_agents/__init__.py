# Conteúdo esperado em 03_manager/sub_agents/__init__.py

# Importa a *instância* do agente de cada módulo
from .idea_agent.agent import idea_agent
from .critic_agent.agent import critic_agent
from .refiner_agent.agent import refiner_agent

# Define o que será importado com "from .sub_agents import *"
__all__ = ["idea_agent", "critic_agent", "refiner_agent"]