from app.config import GROQ_MODEL
from app.services.groq_client import call_llama

class DeveloperAgent:
    def __init__(self):
        self.name = "Developer Agent"
        self.description = "Helps with code bugs, development tasks, and tech support."
        self.system_prompt = (
            "You are a professional software engineer agent who assists with bug fixes, "
            "API responses, code review, and general developer support. Respond with clarity and exact code where needed."
        )

    async def handle_task(self, task: str):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": task}
        ]
        reply = await call_llama(messages)
        return reply
