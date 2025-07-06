from fastapi import FastAPI

# Safe imports using full relative path
from app.api import developer, agents, llama, manager, accountant

app = FastAPI(title="Verexa 🧠 Agentic OS")

# Include all routers
app.include_router(llama.router)
app.include_router(developer.router)
app.include_router(agents.router)
app.include_router(manager.router)
app.include_router(accountant.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Verexa 🧠✨"}
