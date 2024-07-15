from app.schemas.example_schema import ExampleSchema
from app.utils.unitofwork import IUnitOfWork


class ExampleService:

    async def add_obj(self, uow: IUnitOfWork, example: ExampleSchema):
        examples_dict = example.model_dump()
        async with uow:
            example_id = await uow.examples.add_one(examples_dict)
            await uow.commit()
            return example_id

    async def get_objs(self, uow: IUnitOfWork):
        async with uow:
            examples = await uow.examples.find_all()
            return examples

    async def get_obj(self, uow: IUnitOfWork, example_id: int):
        async with uow:
            examples = await uow.examples.find_one(id=example_id)
            return examples

    async def edit_obj(self, uow: IUnitOfWork, example_id: int, example: ExampleSchema):
        examples_dict = example.model_dump()
        async with uow:
            cur_example = await uow.examples.find_one(id=example_id)
            if examples_dict["name"] is None:
                examples_dict["name"] = cur_example.title
            await uow.examples.edit_one(example_id, examples_dict)
            await uow.commit()

    async def delete_obj(self, uow: IUnitOfWork, example_id: int):
        async with uow:
            await uow.examples.delete_one(example_id)
            await uow.commit()
