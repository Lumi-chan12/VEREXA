# app/core/team_leader_agent.py

class TeamLeaderAgent:
    def __init__(self):
        self.available_agents = {
            "developer": "DeveloperAgent",
            "manager": "ManagerAgent",
            "accountant": "AccountantAgent"
        }

    def assign_task(self, task: str) -> str:
        task = task.lower()
        if "code" in task or "fix" in task:
            assigned_to = self.available_agents["developer"]
        elif "inventory" in task or "stock" in task:
            assigned_to = self.available_agents["manager"]
        elif "profit" in task or "bill" in task:
            assigned_to = self.available_agents["accountant"]
        else:
            assigned_to = "UnknownAgent"
        
        return f"TeamLeader assigned the task to: {assigned_to}"
