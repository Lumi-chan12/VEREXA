from fastapi import FastAPI
from fastapi.responses import FileResponse

# Safe imports using full relative path
from app.api import developer, agents, llama, manager, accountant, support, customer, logistics, marketing, llama, speech
from app.services.coral_core import coral_decision
from app.core.agents_bootstrap import AGENTS

app = FastAPI(title="Verexa 🧠 Agentic OS")

available_agents = AGENTS

# Include all routers
app.include_router(llama.router)
app.include_router(developer.router)
app.include_router(agents.router)
app.include_router(manager.router)
app.include_router(accountant.router)
app.include_router(support.router)
app.include_router(customer.router)
app.include_router(logistics.router)
app.include_router(marketing.router)
app.include_router(speech.router)

@app.get("/")
def test_ui():
    return FileResponse("test_ui.html")