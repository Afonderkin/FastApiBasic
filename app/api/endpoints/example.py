from typing import List, Annotated

from fastapi import APIRouter, Depends

from app import settings
from app.schemas.example_schema import ExampleSchema, ExampleSchemaRead
from app.services.example_service import ExampleService
from app.utils.dependencies import UOWDep

router = APIRouter(
    prefix=settings.API_EXAMPLE__PREFIX,
    tags=[settings.EXAMPLE__TAG],
)


@router.get("")
async def read_examples(
        uow: UOWDep,
) -> List[ExampleSchemaRead]:
    examples = await ExampleService().get_objs(uow)
    return examples


@router.get("/{id}")
async def read_example(
        uow: UOWDep,
        id: int
) -> List[ExampleSchemaRead]:
    example = await ExampleService().get_obj(uow, id)
    return example


@router.post("/create")
async def create_example(
        uow: UOWDep,
        example: Annotated[ExampleSchema, Depends()],
) -> dict:
    example_id = await ExampleService().add_obj(uow, example)
    return {"example_id": example_id}


@router.patch("/{id}")
async def edit_example(
        id: int,
        uow: UOWDep,
        example: Annotated[ExampleSchema, Depends()],
) -> dict:
    await ExampleService().edit_obj(uow, id, example)
    return {"status": "ok"}


@router.delete("/{id}")
async def delete_example(
        id: int,
        uow: UOWDep,
        example: Annotated[ExampleSchema, Depends()],
) -> dict:
    await ExampleService().delete_obj(uow, id)
    return {"status": "ok"}
