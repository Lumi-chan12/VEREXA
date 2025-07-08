from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.core.team_leader_agent import TeamLeaderAgent
from app.core.support_agent import SupportAgent
from app.core.customer_agent import CustomerAgent
from app.core.logistics_agent import LogisticsAgent
from app.core.marketing_agent import MarketingAgent
from app.core.accountant_agent import AccountantAgent
from app.core.manager_agent import ManagerAgent
from app.core.developer_agent import DeveloperAgent

router = APIRouter(prefix="/agents", tags=["Agents"])

# Instantiate all agents
agents = {
    "support": SupportAgent(),
    "customer": CustomerAgent(),
    "logistics": LogisticsAgent(),
    "marketing": MarketingAgent(),
    "accountant": AccountantAgent(),
    "manager": ManagerAgent(),
    "team_leader": TeamLeaderAgent(),
    "developer": DeveloperAgent()
}

# Create an instance of team leader agent
team_lead = TeamLeaderAgent()

class TaskRequest(BaseModel):
    task: str

@router.post("/assign")
async def assign_task_to_agent(request: TaskRequest):
    result = await team_lead.assign_task(request.task)
    if not result:
        raise HTTPException(status_code=404, detail="No agent assigned or task failed")
    return {"assigned": result}
