from fastapi import APIRouter, Depends

from Models.Transcribe import TranscricaoRequest, TranscricaoResponse
from Service.TokenService import auth_login
from Service.TranscricaoService import transcribe_audio

transcricao = APIRouter(tags=["Transcrição"])

@transcricao.post("/transcrever", response_model=TranscricaoResponse)
def transcribe_audio_to_text(request: TranscricaoRequest, user = Depends(auth_login)):
    url = request.url
    audio_text = transcribe_audio(url)

    return TranscricaoResponse(audio_text=audio_text)