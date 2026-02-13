from fastapi import FastAPI

from Router import foo

app = FastAPI(title="API - Transcrição de Áudios", openapi_url="/scomptec", docs_url="/")

app.include_router(foo.router)

