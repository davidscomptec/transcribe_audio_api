from datetime import timedelta, datetime, timezone

from fastapi import Depends
from jose import jwt, JWTError
from starlette import status
from starlette.exceptions import HTTPException

from service.hash_service import verify_client_secret
from service.user_service import get_user_client_id
from config.token_config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM, oauth2_scheme
from models.user import User
from models.token import GetTokenResponse


def create_token(headers):
    user = get_user_client_id(headers.client_id)
    auth_user = verify_client_secret(user['client_secret'], headers.client_secret)

    if not user or not auth_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="ClienteID e/ou ClientSecret inválidos",
        )

    access_token, expire = create_access_token(
        data={"sub": headers.client_id},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return GetTokenResponse(
        access_token=access_token,
        token_type="Bearer",
        expires_in=expire)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire_now = datetime.now() + (expires_delta or timedelta(minutes=15))
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM), expire_now


def auth_login(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        client_id: str = payload.get("sub")

        if client_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        user = get_user_client_id(client_id)
        return User (
            client_id=client_id,
            client_secret=user.get("client_secret"),
            roles=user.get("roles"),
        )

    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Não autorizado: Token inválido {e.args}")

def is_adm(user: User):

    if "ADM" not in user.roles:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário sem permissão para esse método")

    return True
