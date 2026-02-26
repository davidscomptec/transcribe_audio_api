import requests
from typing import Annotated
from fastapi import HTTPException, Header
from config.env import auth_api_url
from models.auth import AuthRequest

def auth_login(headers: Annotated[AuthRequest, Header()]):
    response = requests.get(
        auth_api_url + '/api/token/validate',
        headers={
            'Authorization': 'Bearer ' + headers.token,
        })

    if response.status_code == 200:
        return
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.json()['detail'])