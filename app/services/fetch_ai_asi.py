# app/services/fetch_ai_asi.py
import requests

ASI_ONE_ENDPOINT = "https://asi.fetch.ai/v1/ask"  # (placeholder endpoint)

def ask_asi(task: str) -> str:
    response = requests.post(ASI_ONE_ENDPOINT, json={"query": task})
    return response.json().get("answer", "No response from ASI.")
