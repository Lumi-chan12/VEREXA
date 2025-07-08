from uagents import Agent, Context
from pydantic import BaseModel


# Agent name and seed (secure this in production)
marketing_agent = Agent(
    name="MarketingAgent",
    seed="marketing agent seed phrase",  # Replace this securely
    port=8001,  # Give a different port for each agent
    endpoint="http://127.0.0.1:8001/submit"
)

class MarketingMessage(BaseModel):
    content: str

@marketing_agent.on_event("startup")
async def startup(ctx: Context):
    ctx.logger.info("📢 Marketing Agent is now running and ready!")

@marketing_agent.on_message(MarketingMessage)
async def handle_task(ctx: Context, msg: MarketingMessage):
    response = f"✅ MarketingAgent received: {msg.content}"
    ctx.logger.info(response)
    await ctx.send(msg.sender, MarketingMessage(content=response))


if __name__ == "__main__":
    marketing_agent.run()
