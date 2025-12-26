"""
SAFE MODE – MOCK LLM CLIENT
This file is used during OS bring-up and agent testing.
No external API calls. No paid services.
"""

def call_llama(messages):
    # Extract last user message safely
    user_msg = ""
    for m in messages:
        if m.get("role") == "user":
            user_msg = m.get("content", "")

    return f"[MOCK LLM] Processed request: {user_msg}"


def generate_response(user_input: str, system_prompt: str) -> str:
    return (
        "[MOCK RESPONSE]\n"
        f"System Prompt: {system_prompt}\n"
        f"User Input: {user_input}\n"
        "Status: Agent logic executed successfully."
    )


async def self_refine(response: str) -> str:
    return f"[MOCK REFINEMENT]\n{response}"

# -------------------------------
# OPTIONAL FEATURES (SAFE STUBS)
# -------------------------------

def transcribe_audio(audio_bytes: bytes) -> str:
    """
    Speech-to-text stub (disabled in safe mode)
    """
    return "[SPEECH DISABLED] Audio transcription not available."


def synthesize_speech(text: str) -> bytes:
    """
    Text-to-speech stub (disabled in safe mode)
    """
    return b""
