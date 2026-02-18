from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from fastapi import HTTPException
from starlette import status

crypt = PasswordHasher()


def hash_client_secret(client_secret: str):
    try:
        hashed_client_secret = crypt.hash(client_secret)
        return hashed_client_secret
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error hashing client_secret: {e}")


def verify_client_secret(hashed_client_secret: str, client_secret: str):
    try:
        crypt.verify(hashed_client_secret, client_secret)
        return True
    except VerifyMismatchError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas!"
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Erro ao validar credenciais!"
        )