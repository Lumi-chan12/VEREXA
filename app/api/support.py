# app/api/support.py

from fastapi import APIRouter, Body
from pydantic import BaseModel
from app.core import support_agent

router = APIRouter(prefix="/support", tags=["SupportAgent"])
router = APIRouter(prefix="/support", tags=["support"])

@router.post("/assist")
def get_support_response(query: str = Body(..., embed=True)):
    reply = support_agent.generate_support_response(query)
    return {"response": reply}

@router.get("/test")
async def test_marketing_agent(task: str):
    agent = support_agent()
    response = await agent.respond_to(task)
    return {"response": response}

# ✅ Define this BEFORE using it in the route
class TaskRequest(BaseModel):
    task: str

@router.post("/developer/ask")
async def ask_developer(request: TaskRequest):
    agent = support_agent()
    response = await agent.handle_task(request.task)
    return {"response": response}
