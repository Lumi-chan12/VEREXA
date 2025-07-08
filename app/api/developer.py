from fastapi import APIRouter
from pydantic import BaseModel
from app.core.developer_agent import DeveloperAgent

router = APIRouter(prefix="/agent/dev", tags=["Developer Agent"])
agent = DeveloperAgent()
router = APIRouter(prefix="/developer", tags=["Developer"])

class TaskInput(BaseModel):
    task: str

@router.post("/task")
async def developer_task(input: TaskInput):
    reply = await agent.handle_task(input.task)
    return {"agent": agent.name, "reply": reply}

@router.get("/test")
async def test_marketing_agent(task: str):
    agent = DeveloperAgent()
    response = await agent.respond_to(task)
    return {"response": response}

# ✅ Define this BEFORE using it in the route
class TaskRequest(BaseModel):
    task: str
    
@router.post("/developer/ask")
async def ask_developer(request: TaskRequest):
    return {"response": await agent.handle_task(request.task)}
