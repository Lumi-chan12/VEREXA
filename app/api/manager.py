# app/api/manager.py

from fastapi import APIRouter, Query
from pydantic import BaseModel
from app.core.manager_agent import ManagerAgent

router = APIRouter(prefix="/agent/manager", tags=["Manager Agent"])
router = APIRouter(prefix="/manager", tags=["Manager"])

agent = ManagerAgent()

@router.post("/update")
def update_stock(item: str = Query(...), quantity: int = Query(...)):
    return {"response": agent.update_stock(item, quantity)}

@router.get("/get")
def get_stock(item: str = Query(None)):
    return {"response": agent.get_stock(item)}

@router.get("/check-low")
def check_low_stock(threshold: int = 10):
    return {"response": agent.check_low_stock(threshold)}

@router.get("/test")
async def test_marketing_agent(task: str):
    agent = ManagerAgent()
    response = await agent.respond_to(task)
    return {"response": response}


# ✅ Define this BEFORE using it in the route
class TaskRequest(BaseModel):
    task: str


@router.post("/manager/ask")
async def ask_manager(request: TaskRequest):
    return {"response": await agent.handle_task(request.task)}