from pydantic import BaseModel


class TranscricaoRequest(BaseModel):
    url: str

class TranscricaoResponse(BaseModel):
    audio_text: str