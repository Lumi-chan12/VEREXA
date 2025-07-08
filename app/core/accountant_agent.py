

# app/core/accountant_agent.py

from datetime import datetime
from app.core.memory_manager import get_context, add_to_context
from app.services.groq_client import call_llama, self_refine

SYSTEM_PROMPT = "You are a detail-oriented business accountant AI skilled in finance, taxes, and bookkeeping."

class AccountantAgent:
    def __init__(self):
        self.name = "Accountant Agent"
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


ledger = []

def record_transaction(transaction_type: str, amount: float, description: str):
    entry = {
        "type": transaction_type.lower(),
        "amount": amount,
        "description": description,
        "timestamp": datetime.utcnow().isoformat()
    }
    ledger.append(entry)
    return f"✅ Recorded {transaction_type} of ₹{amount} for: {description}"

def calculate_profit_loss():
    income = sum(entry["amount"] for entry in ledger if entry["type"] == "income")
    expense = sum(entry["amount"] for entry in ledger if entry["type"] == "expense")
    return {
        "income": income,
        "expense": expense,
        "profit_or_loss": income - expense
    }

def get_ledger():
    return ledger
