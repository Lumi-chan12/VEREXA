from app.core.agent_registry import AGENTS
from app.services.coral_core import coral_decision
from app.core.memory_manager import get_context, add_to_context
from app.services.groq_client import call_llama, self_refine


class TeamLeaderAgent:
    def __init__(self):
        self.name = "Team Leader Agent"
        self.system_prompt = (
            "You're the team lead. Based on the task, decide which agent should handle it. "
            "Only return one of the following keywords: support, customer, logistics, marketing, "
            "accountant, manager, developer."
        )
        self.available_agents = AGENTS  # Use centralized registry

    async def assign_task(self, task: str) -> dict:
        add_to_context(self.name, "user", task)

        selected_key = coral_decision(task)
        agent = self.available_agents.get(selected_key)

        print(f"[TeamLeader] ➜ Assigning to: {selected_key}")

        if not agent:
            return {
                "assigned_to": None,
                "response": "❌ No agent found.",
                "coral_metadata": f"[CORAL] Invalid assignment: '{selected_key}'"
            }

        response = await agent.handle_task(task)
        add_to_context(self.name, "assistant", response)

        return {
            "assigned_to": selected_key,
            "response": response,
            "coral_metadata": f"[CORAL] Task '{task}' ➜ Assigned to: {selected_key}"
        }
