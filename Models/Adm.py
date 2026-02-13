from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    client_id: str
    roles: str

class CreateUserResponse(BaseModel):
    client_id: str
    client_secret: str
    roles: str