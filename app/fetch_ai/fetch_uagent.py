from uagents import Agent, Context
import os

# Create a Fetch.ai-compatible agent
fetch_ai_agent = Agent(
    name="verexa-fetch-agent",
    seed=os.getenv("FETCH_SEED", "verexa_secret_seed_123"),  # secure this in real projects
)

# This defines what happens when this agent receives a message
@fetch_ai_agent.on_message()
async def handle_message(ctx: Context, sender: str, msg: str):
    ctx.logger.info(f"🔁 Received: {msg} from {sender}")
    # Example logic
    if "inventory" in msg:
        await ctx.send(sender, "Our stock is 85% full. Next dispatch is at 3 PM.")
    else:
        await ctx.send(sender, f"Echoing your message: {msg}")
