from app.config import GROQ_API_KEY, GROQ_MODEL
import httpx
import io
import io
from whisper import load_model
from scipy.io.wavfile import write as write_wav
from bark import SAMPLE_RATE, generate_audio
import numpy as np

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

async def call_llama(messages: list):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "messages": messages,
        "temperature": 0.7
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(GROQ_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]

def generate_response(user_input: str, system_prompt: str) -> str:
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]
    import asyncio
    return asyncio.run(call_llama(messages))

async def self_refine(response: str) -> str:
    """
    Compound-Beta: Sends agent's initial response back to the model with a prompt asking for improvement.
    """
    reflection_prompt = (
        "Here is the initial assistant response:\n"
        f"""{response}"""
        "\n\nCan you revise or improve this response to make it clearer, more complete, or more helpful?"
    )
    messages = [
        {"role": "system", "content": "You are a reflective AI that improves assistant responses."},
        {"role": "user", "content": reflection_prompt}
    ]
    return await call_llama(messages)


def transcribe_audio(audio_bytes):
    model = load_model("base")
    audio = np.frombuffer(audio_bytes, dtype=np.int16)
    result = model.transcribe(audio=audio, language="en")
    return result["text"]

def synthesize_speech(text):
    audio_array = generate_audio(text)
    wav_io = io.BytesIO()
    write_wav(wav_io, SAMPLE_RATE, audio_array)
    wav_io.seek(0)
    return wav_io.read()