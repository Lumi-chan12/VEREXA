# app/core/agents_bootstrap.py

from app.core.developer_agent import DeveloperAgent
from app.core.marketing_agent import MarketingAgent
from app.core.manager_agent import ManagerAgent
from app.core.customer_agent import CustomerAgent
from app.core.support_agent import SupportAgent
from app.core.logistics_agent import LogisticsAgent
from app.core.accountant_agent import AccountantAgent

AGENTS = {
    "developer": DeveloperAgent(),
    "marketing": MarketingAgent(),
    "manager": ManagerAgent(),
    "customer": CustomerAgent(),
    "support": SupportAgent(),
    "logistics": LogisticsAgent(),
    "accountant": AccountantAgent()
}
