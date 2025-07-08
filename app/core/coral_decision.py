# app/core/coral_decision.py

def coral_decision(task: str) -> str:
    # Very basic fallback logic (you can replace with real logic)
    keywords = {
        "refund": "support",
        "invoice": "accountant",
        "bug": "developer",
        "delivery": "logistics",
        "marketing": "marketing",
        "feature": "customer",
        "manager": "manager"
    }
    for key, val in keywords.items():
        if key in task.lower():
            return val
    return "support"  # default fallback
