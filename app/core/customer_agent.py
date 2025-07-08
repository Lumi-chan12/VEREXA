# app/core/customer_agent.py

from app.core.memory_manager import get_context, add_to_context
from app.services.groq_client import call_llama, self_refine

class CustomerAgent:
    def __init__(self):
        self.name = "Customer Agent"
        self.system_prompt = (
            "You are a helpful customer service AI. Help customers with their orders, "
            "account queries, and provide relevant and friendly information."
        )
        self.responses = {
            "pricing": "Sure! You can find our pricing plans on the Pricing page.",
            "features": "Verexa helps businesses build a website and run an AI-powered virtual team.",
            "support": "You can reach out to us anytime via our Help Center or live chat.",
            "default": "I’m happy to assist you! Could you please clarify your question?"
        }

    def handle_question(self, question: str) -> str:
        q = question.lower()
        if "price" in q:
            return self.responses["pricing"]
        elif "feature" in q or "do" in q:
            return self.responses["features"]
        elif "help" in q or "support" in q:
            return self.responses["support"]
        else:
            return self.responses["default"]

    async def handle_task(self, task: str) -> str:
        add_to_context(self.name, "user", task)

        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(get_context(self.name))
        messages.append({"role": "user", "content": task})

        first_reply = await call_llama(messages)
        refined_reply = await self_refine(first_reply)

        add_to_context(self.name, "assistant", refined_reply)
        return refined_reply

