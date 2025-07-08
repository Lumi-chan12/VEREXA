# app/core/marketing_agent.py

from app.services.groq_client import call_llama, self_refine
from app.core.memory_manager import get_context, add_to_context

SYSTEM_PROMPT = "You are a creative and trendy marketing AI that crafts social media posts, ad copy, and email campaigns."

TONE_PRESETS = {
    "casual": "Write in a casual, friendly, Gen-Z voice.",
    "professional": "Write in a formal, business-professional tone.",
    "excited": "Use energetic, fun, and slightly dramatic tone.",
    "minimal": "Be very short, clean, and modern in tone."
}

class MarketingAgent:
    def __init__(self):
        self.name = "Marketing Agent"
        self.system_prompt = SYSTEM_PROMPT

    async def respond_to(self, task: str) -> str:
        add_to_context(self.name, "user", task)
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(get_context(self.name))
        messages.append({"role": "user", "content": task})
        reply = await call_llama(messages)
        add_to_context(self.name, "assistant", reply)
        return reply

    def generate_social_post_prompt(self, product: str, tone: str = "casual") -> str:
        tone_instruction = TONE_PRESETS.get(tone.lower(), TONE_PRESETS["casual"])
        return f"{tone_instruction}\nCreate a short LinkedIn or Instagram post promoting this: {product}."

    def generate_ad_copy_prompt(self, product: str, audience: str) -> str:
        return f"Create a catchy ad copy for '{product}' targeting '{audience}'. Keep it punchy and action-driven."

    def generate_email_campaign_prompt(self, product: str, feature: str, goal: str) -> str:
        return (
            f"Write a marketing email to promote '{product}', highlighting the feature '{feature}'. "
            f"The goal is to '{goal}'. Make it engaging and suitable for email readers."
        )

    async def handle_task(self, task: str):
        add_to_context(self.name, "user", task)
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(get_context(self.name))
        messages.append({"role": "user", "content": task})

        first_reply = await call_llama(messages)
        refined_reply = await self_refine(first_reply)

        add_to_context(self.name, "assistant", refined_reply)
        return refined_reply