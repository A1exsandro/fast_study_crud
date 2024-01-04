import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import db


def init_app():
    db.init()

    app = FastAPI(
        title="Study Fast",
        description="CRUD",
        version="1"
    )

    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    
    @app.on_event("startup")
    async def startup():
        await db.create_all()

    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    from app.router import tipo_equipamento

    app.include_router(tipo_equipamento.router)
    
    return app

app = init_app()
