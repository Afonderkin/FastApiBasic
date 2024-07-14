from sqlalchemy.orm import Session
from app.models.example_model import ExampleModel


class ExampleRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_example(self, example_id: int):
        return self.db.query(ExampleModel).filter(ExampleModel.id == example_id).first()
