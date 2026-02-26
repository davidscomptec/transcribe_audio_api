from pydantic import BaseModel, Field


class TranscricaoRequest(BaseModel):
    url: str = Field(title='url', examples=['https://urldoseuaduio.com/download'])

class TranscricaoResponse(BaseModel):
    audio_text: str = Field(title='audio_text', examples=['Áudio transcrito'])