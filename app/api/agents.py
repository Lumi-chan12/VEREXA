from fastapi import APIRouter
from pydantic import BaseModel
from app.core.team_leader_agent import TeamLeaderAgent

router = APIRouter(prefix="/agents", tags=["Agents"])
team_lead = TeamLeaderAgent()

class TaskRequest(BaseModel):
    task: str

@router.post("/assign")
def assign_task_to_agent(request: TaskRequest):
    result = team_lead.assign_task(request.task)
    return {"assigned": result}
