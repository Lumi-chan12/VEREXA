# app/api/logistics.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.logistics_agent import LogisticsAgent

router = APIRouter()
agent = LogisticsAgent()
router = APIRouter(prefix="/logistics", tags=["logistics"])

class LogisticsRequest(BaseModel):
    message: str

@router.post("/logistics")
def logistics_response(req: LogisticsRequest):
    try:
        reply = agent.handle_logistics(req.message)
        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/test")
async def test_marketing_agent(task: str):
    agent = LogisticsAgent()
    response = await agent.respond_to(task)
    return {"response": response}
