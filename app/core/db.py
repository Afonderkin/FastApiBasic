from app import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_async_engine(settings.DATABASE_URL, future=settings.FUTURE)
AsyncSessionLocal = sessionmaker(engine,
                                 expire_on_commit=settings.EXPIRE_ON_COMMIT,
                                 class_=AsyncSession)


Base = declarative_base()


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db
        await db.commit()
