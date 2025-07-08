# app/api/accountant.py

from fastapi import APIRouter, Query
from app.core import accountant_agent

router = APIRouter(prefix="/agent/accountant", tags=["Accountant Agent"])
router = APIRouter(prefix="/accountant", tags=["accountant"])

@router.post("/record")
def record_transaction(
    transaction_type: str = Query(..., enum=["income", "expense"]),
    amount: float = Query(...),
    description: str = Query(...)
):
    response = accountant_agent.record_transaction(transaction_type, amount, description)
    return {"response": response}

@router.get("/summary")
def get_summary():
    return {"response": accountant_agent.calculate_profit_loss()}

@router.get("/ledger")
def get_ledger():
    return {"response": accountant_agent.get_ledger()}

@router.get("/test")
async def test_marketing_agent(task: str):
    agent = accountant_agent()
    response = await agent.respond_to(task)
    return {"response": response}