from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.developer_agent import DeveloperAgent

router = APIRouter(prefix="/agent/dev", tags=["Developer Agent"])
agent = DeveloperAgent()

class TaskInput(BaseModel):
    task: str

@router.post("/task")
async def developer_task(input: TaskInput):
    reply = await agent.handle_task(input.task)
    return {"agent": agent.name, "reply": reply}
