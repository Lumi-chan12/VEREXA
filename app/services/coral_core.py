# app/services/coral_core.py

def coral_decision(task: str) -> str:
    """
    Basic Coral Protocol decision simulation.
    In real cases, this could be DAO logic, decentralized data access, or governance logic.
    """
    if "governance" in task.lower():
        return "manager"
    elif "wallet" in task.lower() or "crypto" in task.lower():
        return "accountant"
    elif "community" in task.lower() or "DAO" in task.lower():
        return "support"
    else:
        return "marketing"  # fallback for Coral community engagement
# app/services/coral_core.py

def coral_decision(task: str) -> str:
    task_lower = task.lower()

    if any(keyword in task_lower for keyword in ["bug", "fix", "code", "develop", "python", "async"]):
        return "developer"
    elif any(keyword in task_lower for keyword in ["invoice", "balance", "finance", "payment"]):
        return "accountant"
    elif any(keyword in task_lower for keyword in ["email", "post", "ad", "social", "campaign"]):
        return "marketing"
    elif any(keyword in task_lower for keyword in ["customer", "complaint", "feedback"]):
        return "support"
    elif any(keyword in task_lower for keyword in ["delivery", "track", "shipment", "package"]):
        return "logistics"
    elif any(keyword in task_lower for keyword in ["team", "manage", "supervise", "project"]):
        return "manager"
    else:
        return "support"  # Fallback
