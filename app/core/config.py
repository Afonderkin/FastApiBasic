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

settings = Settings()
