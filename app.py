from fastapi import FastAPI

from router.auth_controller import auth
from router.transcribe_controller import transcricao
from router.user_controller import user

app = FastAPI(title="API - Transcrição de Áudios", openapi_url="/scomptec", docs_url="/")

app.include_router(transcricao)
app.include_router(user)
app.include_router(auth)

