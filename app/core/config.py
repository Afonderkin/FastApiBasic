from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Template"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "A template for FastAPI projects"

    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/dbname"


settings = Settings()
