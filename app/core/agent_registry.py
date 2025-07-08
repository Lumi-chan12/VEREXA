# app/core/agent_registry.py

from app.core.marketing_agent import MarketingAgent
from app.core.support_agent import SupportAgent
from app.core.manager_agent import ManagerAgent
from app.core.customer_agent import CustomerAgent
from app.core.developer_agent import DeveloperAgent
from app.core.accountant_agent import AccountantAgent
from app.core.logistics_agent import LogisticsAgent

AGENTS = {
    "marketing": MarketingAgent(),
    "support": SupportAgent(),
    "manager": ManagerAgent(),
    "customer": CustomerAgent(),
    "developer": DeveloperAgent(),
    "accountant": AccountantAgent(),
    "logistics": LogisticsAgent(),
}
def get_all_agents():
    """Retrieve all registered agents."""
    return AGENTS.values()

def get_agent(agent_name: str):
    """Retrieve an agent instance by name."""
    return AGENTS.get(agent_name.lower())