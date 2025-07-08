import io
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from app.services.groq_client import transcribe_audio, synthesize_speech

router = APIRouter(prefix="/speech", tags=["Speech"])

@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    if not file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="File must be audio")
    audio_bytes = await file.read()
    result = transcribe_audio(audio_bytes)
    return {"transcription": result}

@router.post("/speak")
async def speak(text: str):
    audio_data = synthesize_speech(text)
    return StreamingResponse(io.BytesIO(audio_data), media_type="audio/mpeg")
