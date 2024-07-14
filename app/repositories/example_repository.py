from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.example_model import ExampleModel


class ExampleRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_example(self, example_id: int):
        query = select(ExampleModel).where(ExampleModel.id == example_id)
        result = await self.db.execute(query)
        return result.scalars().first()
