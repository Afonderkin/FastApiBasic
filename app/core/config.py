import logging
from logging.config import dictConfig

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """ Project-settings """
    PROJECT_NAME: str = "FastAPI Template"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "A template for FastAPI projects"

    """ db-settings """
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/dbname"
    EXPIRE_ON_COMMIT: bool = False
    FUTURE: bool = True

    """ Prefix-settings """
    API_V1__PREFIX: str = "/api/v1"

    """ Uvicorn-prefix """
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    """ Logging-settings """
    LOG_LEVEL: int = logging.INFO
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_DATE_FORMAT: str = "%Y-%m-%d %H:%M:%S"
    LOG_FILE: str = "app.log"


settings = Settings()


def configure_logging(settings: Settings):
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": settings.LOG_FORMAT,
                "datefmt": settings.LOG_DATE_FORMAT,
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": settings.LOG_FILE,
                "formatter": "default",
            },
        },
        "root": {
            "handlers": ["console", "file"],
            "level": settings.LOG_LEVEL,
        },
    }
    dictConfig(logging_config)


configure_logging(settings=settings)
