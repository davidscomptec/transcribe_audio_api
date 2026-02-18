from fastapi import APIRouter, Depends

from models.transcribe import TranscricaoRequest, TranscricaoResponse
from service.token_service import auth_login
from service.transcricao_service import transcribe_audio

transcricao = APIRouter(tags=["Transcrição"])

@transcricao.post("/transcrever", response_model=TranscricaoResponse)
def transcribe_audio_to_text(request: TranscricaoRequest, user = Depends(auth_login)):
    url = request.url
    audio_text = transcribe_audio(url)

    return TranscricaoResponse(audio_text=audio_text)