from app.api import developer
from fastapi import FastAPI
from app.api import agents
from app.api import llama
app.include_router(llama.router)
app.include_router(developer.router)

app = FastAPI(title="Verexa – Agentic OS")

# Include the router
app.include_router(agents.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Verexa 🧠✨"}
