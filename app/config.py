# Future config will go here
from dotenv import load_dotenv
import os

load_dotenv()  # load from .env

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = os.getenv("GROQ_API_URL")
GROQ_MODEL = os.getenv("GROQ_MODEL")
