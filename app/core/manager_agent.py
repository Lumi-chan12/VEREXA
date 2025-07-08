# app/core/manager_agent.py

from typing import Dict, Optional
from app.services.groq_client import call_llama, self_refine
from app.core.memory_manager import get_context, add_to_context

SYSTEM_PROMPT = "You are a strategic and professional business manager AI who helps with operations, decision-making, and team coordination."

class ManagerAgent:
    def __init__(self):
        self.name = "Manager Agent"
        self.system_prompt = SYSTEM_PROMPT
        self.inventory: Dict[str, int] = {
            "Laptops": 10,
            "Mice": 25,
            "Notebooks": 50
        }

    def update_stock(self, item: str, quantity: int) -> str:
        self.inventory[item] = quantity
        return f"✅ Updated stock for {item} to {quantity} units."

    def get_stock(self, item: Optional[str] = None) -> str:
        if item:
            qty = self.inventory.get(item)
            if qty is not None:
                return f"{item} has {qty} units in stock."
            return f"{item} is not found in inventory."
        else:
            return "📦 Inventory Report:\n" + "\n".join(f"- {i}: {q} units" for i, q in self.inventory.items())

    def check_low_stock(self, threshold: int = 10) -> str:
        low = [i for i, q in self.inventory.items() if q < threshold]
        if low:
            return "⚠️ Low Stock Alert:\n" + "\n".join(f"- {i}" for i in low)
        return "✅ All stock levels are sufficient."

    async def handle_task(self, task: str) -> str:
        add_to_context(self.name, "user", task)

        if "escalate" in task.lower():
            # 🔁 Delayed import to avoid circular import
            from app.core.message_router import send_message
            support_response = await send_message("support", "Escalation requested by Manager: " + task)
            return f"📤 Escalation sent to Support Agent. Response: {support_response}"

        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(get_context(self.name))
        messages.append({"role": "user", "content": task})

        first_reply = await call_llama(messages)
        refined_reply = await self_refine(first_reply)

        add_to_context(self.name, "assistant", refined_reply)
        return refined_reply
