# app/api/customer.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.customer_agent import CustomerAgent

router = APIRouter()
agent = CustomerAgent()
router = APIRouter(prefix="/customer", tags=["customer"])

class CustomerRequest(BaseModel):
    question: str

@router.post("/customer")
def ask_customer_agent(req: CustomerRequest):
    try:
        reply = agent.handle_question(req.question)
        return {"answer": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/test")
async def test_marketing_agent(task: str):
    agent = CustomerAgent()
    response = await agent.respond_to(task)
    return {"response": response}


# ✅ Define this BEFORE using it in the route
class TaskRequest(BaseModel):
    task: str

    
@router.post("/customer/ask")
async def ask_customer(request: TaskRequest):
    return {"response": await agent.handle_task(request.task)}
