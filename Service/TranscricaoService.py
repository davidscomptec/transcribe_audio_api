import io

import whisper
import librosa
import requests
from whisper import transcribe

def transcribe_audio(url):
    response = requests.get(url)
    audio_data = io.BytesIO(response.content)

    audio, sr = librosa.load(audio_data)

    model = whisper.load_model("small")

    result = transcribe(model, audio)
    return result["text"]