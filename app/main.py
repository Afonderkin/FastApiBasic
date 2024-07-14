import uvicorn

from app import create_app, settings


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
