# app/core/memory_manager.py

from collections import defaultdict, deque

# Stores recent messages for each agent/session
memory_store = defaultdict(lambda: deque(maxlen=10))  # limit to last 10 messages

def get_context(agent_name: str):
    """Returns recent memory for the given agent"""
    return list(memory_store[agent_name])

def add_to_context(agent_name: str, role: str, content: str):
    """Adds a message to the agent's memory"""
    memory_store[agent_name].append({
        "role": role,
        "content": content
    })

def clear_context(agent_name: str):
    """Clears context for an agent"""
    memory_store[agent_name].clear()

# app/core/memory_manager.py

# Basic memory structure to simulate "context" memory for agents
context_store = {}

def add_to_context(agent_name: str, role: str, content: str):
    if agent_name not in context_store:
        context_store[agent_name] = []
    context_store[agent_name].append({"role": role, "content": content})
    # Limit memory to last 10 exchanges
    context_store[agent_name] = context_store[agent_name][-10:]

def get_context(agent_name: str):
    return context_store.get(agent_name, [])
