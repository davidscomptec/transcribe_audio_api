import io

import whisper
import librosa
import requests
from starlette import status
from starlette.exceptions import HTTPException
from whisper import transcribe

def transcribe_audio(url):
    try:
        response = requests.get(url)
        audio_data = io.BytesIO(response.content)

        audio, sr = librosa.load(audio_data)

        model = whisper.load_model("base")

        result = transcribe(model, audio)
        return result["text"]
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao transcrever audio: {e}"
        )