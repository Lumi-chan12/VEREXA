from fastapi import APIRouter
from pydantic import BaseModel
from app.services.groq_client import call_llama

router = APIRouter(prefix="/llama", tags=["LLaMA"])

class LlamaPrompt(BaseModel):
    prompt: str

@router.post("/chat")
async def llama_chat(req: LlamaPrompt):
    messages = [{"role": "user", "content": req.prompt}]
    reply = await call_llama(messages)
    return {"reply": reply}
