from app.models.example_model import ExampleModel
from app.repositories.base_repository import BaseRepository


class ExampleRepository(BaseRepository):

    model = ExampleModel
