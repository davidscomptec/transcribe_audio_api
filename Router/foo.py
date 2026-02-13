from fastapi import APIRouter

from Controller.UserController import user
from Controller.AuthController import auth
from Controller.TranscribeController import transcricao

router = APIRouter()

router.include_router(transcricao)
router.include_router(user)
router.include_router(auth)

