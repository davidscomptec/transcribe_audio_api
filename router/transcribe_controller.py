from typing import Annotated

from fastapi import APIRouter, Depends, Body

from models.transcribe import TranscricaoRequest, TranscricaoResponse
from service.auth_service import auth_login
from service.transcricao_service import transcribe_audio

transcricao = APIRouter(tags=['Transcrição'])

@transcricao.post('/transcrever',
                  response_model=TranscricaoResponse,
                  dependencies=[Depends(auth_login)],
                  description='Deve ser informado o link do áudio a ser transcrito e retornará a transcrição '
                              '(O Token deve ser obtido através da AuthAPI)')
def transcribe_audio_to_text(request: TranscricaoRequest):
    url = request.url
    audio_text = transcribe_audio(url)
    return TranscricaoResponse(audio_text=audio_text)