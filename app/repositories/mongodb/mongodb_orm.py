from ..repository import Repository
from pymongo.collection import Collection
from pydantic import BaseModel

class MongoDBORM(Repository):
    """
    The parent class that performs general CRUD operations on MongoDB in the given repository.
    """

    _repository: Collection

    def __init__(self, repository: Collection) -> None:
        self._repository = repository

    def insert(self, model: BaseModel) -> None:
        """
        Inserts a data_model into the given <self._repository>.
        """
        self._repository.insert_one(model.model_dump())

    def get(self, filter: dict) -> dict | None:
        """
        Retrieves a data_model from <self._repository> with the applied filter.
        """
        return self._repository.find_one(filter)

    def get_all(self, filter: dict) -> list[dict]:
        """
        Retrieves all data_models from <self._repository> with the applied filter.
        """
        return list(self._repository.find(filter))

    def delete(self, filter: dict) -> bool:
        """
        Deletes a data_model from <self._repository> with the applied filter.
        """
        res = self._repository.delete_one(filter)
        return res.acknowledged

    def update(self, query: dict, new_data: dict) -> None:
        """
        Updates a data_model from <self._repository> with the applied filter.
        """
        self._repository.update_one(query, new_data)

    def exists(self, query: dict) -> bool:
        """
        Check if a model exists in <self._repository> using the given filter.
        """
        return False if not self.get(query) else True
