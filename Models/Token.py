from datetime import datetime

from pydantic import BaseModel


class GetTokenRequest(BaseModel):
    client_id: str
    client_secret: str

class GetTokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: datetime

class ValidateTokenResponse(BaseModel):
    message: str
    client_id: str
    encrypted_client_secret: str
    roles: list[str]
