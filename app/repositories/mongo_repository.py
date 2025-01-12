from .repository import Repository
from pymongo.collection import Collection
from pydantic import BaseModel

class MongoRepository(Repository):
    """
    Performs general CRUD operations on MongoDB in the given repository.
    """

    _repository: Collection

    def __init__(self, repository: Collection) -> None:
        self._repository = repository

    def insert(self, model: BaseModel) -> None:
        """
        Inserts a data_model into the given <self._repository>.
        """
        self._repository.insert_one(model.model_dump())

    def get(self, filter: dict) -> dict:
        """
        Retrieves a data_model from <self._repository> with the applied filter.
        """
        return self._repository.find_one(filter)

    def get_all(self, filter: dict) -> dict:
        """
        Retrieves all data_models from <self._repository> with the applied filter.
        """
        pass

    def delete(self, filter: dict) -> dict:
        """
        Deletes a data_model from <self._repository> with the applied filter.
        """
        pass

    def update(self, filter: dict) -> dict:
        """
        Updates a data_model from <self._repository> with the applied filter.
        """
        pass