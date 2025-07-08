# app/core/support_agent.py

from app.core.memory_manager import get_context, add_to_context
from app.services.groq_client import call_llama, self_refine

SYSTEM_PROMPT = (
    "You are a helpful Support AI who assists with customer queries, resolves issues, and provides clear, friendly support messages."
)

class SupportAgent:
    def __init__(self):
        self.name = "Support Agent"
        self.system_prompt = SYSTEM_PROMPT

    async def handle_task(self, task: str) -> str:
        add_to_context(self.name, "user", task)

        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(get_context(self.name))
        messages.append({"role": "user", "content": task})

        first_reply = await call_llama(messages)
        refined_reply = await self_refine(first_reply)

        add_to_context(self.name, "assistant", refined_reply)
        return refined_reply
