# app/core/accountant_agent.py

from datetime import datetime

# In-memory financial data
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
    profit = income - expense
    return {
        "income": income,
        "expense": expense,
        "profit_or_loss": profit
    }

def get_ledger():
    return ledger
