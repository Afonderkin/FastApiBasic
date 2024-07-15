from fastapi import FastAPI

from app.core.config import settings
from app.api.endpoints import all_routers


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        description=settings.PROJECT_DESCRIPTION,
    )
    # Include routers
    for router in all_routers:
        app.include_router(router)

    return app
