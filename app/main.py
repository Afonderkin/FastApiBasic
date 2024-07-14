import uvicorn

from app import create_app, settings
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from fastapi import FastAPI

app: "FastAPI" = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
