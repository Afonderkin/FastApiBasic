from app.core.db import Base
from sqlalchemy import Column, Integer, String

from app.schemas.example_schema import ExampleSchemaRead


class ExampleModel(Base):

    __tablename__ = "examples"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    def to_read_model(self):
        return ExampleSchemaRead(id=self.id, name=self.name)
