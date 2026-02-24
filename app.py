from fastapi import FastAPI, APIRouter

from router.transcribe_controller import transcricao

app = FastAPI(title="API - Transcrição de Áudios", openapi_url="/scomptec", docs_url="/")

router = APIRouter(prefix="/api")


router.include_router(transcricao)

app.include_router(router)
