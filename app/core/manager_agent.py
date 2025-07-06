# app/core/manager_agent.py

from typing import Dict, Optional

class ManagerAgent:
    def __init__(self):
        # Local inventory state (can later use Snowflake)
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
            return "📦 Inventory Report:\n" + "\n".join(
                f"- {i}: {q} units" for i, q in self.inventory.items()
            )

    def check_low_stock(self, threshold: int = 10) -> str:
        low = [i for i, q in self.inventory.items() if q < threshold]
        if low:
            return "⚠️ Low Stock Alert:\n" + "\n".join(f"- {i}" for i in low)
        return "✅ All stock levels are sufficient."
