from abc import ABC, abstractmethod
from typing import Type

from app.repositories.example_repository import ExampleRepository


from app.core.db import AsyncSessionLocal


class IUnitOfWork(ABC):
    examples: Type[ExampleRepository]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = AsyncSessionLocal

    async def __aenter__(self):
        self.session = self.session_factory()

        self.examples = ExampleRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()