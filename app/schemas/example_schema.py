from pydantic import BaseModel


class ExampleSchema(BaseModel):
    name: str


class ExampleSchemaRead(ExampleSchema):
    id: int

    class Config:
        from_attributes = True


class ExampleSchemaDelete(BaseModel):
    pass
