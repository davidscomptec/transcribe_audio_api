from typing import Annotated
from fastapi import APIRouter, Header, Depends

from Models.Token import GetTokenRequest, GetTokenResponse, ValidateTokenResponse
from Service.TokenService import create_token, auth_login

auth = APIRouter(tags=["Token"], prefix="/token")


@auth.get("/get", response_model=GetTokenResponse)
def get_token(request_headers: Annotated[GetTokenRequest, Header()]):
    token = create_token(request_headers)
    return token

@auth.get("/validate", response_model=ValidateTokenResponse)
def validate_token(user = Depends(auth_login)):
    return ValidateTokenResponse(
        message="Login Success",
        client_id=user.client_id,
        encrypted_client_secret=user.client_secret,
        roles=user.roles)