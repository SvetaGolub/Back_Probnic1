from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import app
from .config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,

    )

    app.add_middleware()