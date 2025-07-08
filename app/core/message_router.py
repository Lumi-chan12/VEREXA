# app/core/message_router.py

# app/core/message_router.py
from app.core.agents_bootstrap import AGENTS
from app.core.coral_decision import coral_decision

async def send_message(agent_key: str, message: str):
    agent = AGENTS.get(agent_key)
    if not agent:
        return f"❌ Agent '{agent_key}' not found."

    print(f"[Router] ➜ Sending message to {agent_key}: {message}")
    response = await agent.handle_task(message)
    print(f"[{agent_key}] ➜ Replied: {response}")
    return response
async def route_message(task: str) -> dict:
    """
    Routes the task to the appropriate agent based on the task description.
    """
    # Use the coral_decision function to determine which agent should handle the task
    selected_key = coral_decision(task)
    agent = AGENTS.get(selected_key)

    print(f"[MessageRouter] ➜ Assigning to: {selected_key}")

    if not agent:
        return {
            "assigned_to": None,
            "response": "❌ No agent found.",
            "coral_metadata": f"[CORAL] Invalid assignment: '{selected_key}'"
        }

    response = await agent.handle_task(task)
    return {
        "assigned_to": selected_key,
        "response": response,
        "coral_metadata": f"[CORAL] Task '{task}' ➜ Assigned to: {selected_key}"
    }