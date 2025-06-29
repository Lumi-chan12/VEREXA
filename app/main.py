from fastapi import FastAPI
from app.api import agents

app = FastAPI(title="Verexa – Agentic OS")

# Include the router
app.include_router(agents.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Verexa 🧠✨"}
