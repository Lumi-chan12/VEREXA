# app/api/marketing.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.core.marketing_agent import MarketingAgent

router = APIRouter()
agent = MarketingAgent()
router = APIRouter(prefix="/marketing", tags=["Marketing"])

class PostRequest(BaseModel):
    product: str
    tone: str = "casual"

class AdCopyRequest(BaseModel):
    product: str
    audience: str

class EmailRequest(BaseModel):
    product: str
    feature: str
    goal: str

@router.post("/marketing/social-post")
def create_social_post(req: PostRequest):
    try:
        return {"response": agent.generate_social_post(req.product, req.tone)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/marketing/ad-copy")
def create_ad_copy(req: AdCopyRequest):
    try:
        return {"response": agent.generate_ad_copy(req.product, req.audience)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/marketing/email")
def create_email(req: EmailRequest):
    try:
        return {"response": agent.generate_email_campaign(req.product, req.feature, req.goal)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/test")
async def test_marketing_agent(task: str):
    agent = MarketingAgent()
    response = await agent.respond_to(task)
    return {"response": response}


# ✅ Define this BEFORE using it in the route
class TaskRequest(BaseModel):
    task: str


@router.post("/developer/ask")
async def ask_developer(request: TaskRequest):
    response = await agent.handle_task(request.task)
    return {"response": response}
