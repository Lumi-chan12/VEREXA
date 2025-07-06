# app/api/manager.py

from fastapi import APIRouter, Query
from app.core.manager_agent import ManagerAgent

router = APIRouter(prefix="/agent/manager", tags=["Manager Agent"])

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
