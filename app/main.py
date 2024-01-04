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
    
    return app

app = init_app()
