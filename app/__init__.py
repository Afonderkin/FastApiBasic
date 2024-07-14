from fastapi import FastAPI

from app.core.config import settings
from app.api.endpoints import example

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        description=settings.PROJECT_DESCRIPTION,
    )
    # Include routers
    app.include_router(example.router, prefix="/api/v1")

    return app
