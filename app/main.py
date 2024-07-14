import uvicorn

from app import create_app, settings
from typing import TYPE_CHECKING

from app.core.config import configure_logging


if TYPE_CHECKING:
    from fastapi import FastAPI


configure_logging(settings)
app: "FastAPI" = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
