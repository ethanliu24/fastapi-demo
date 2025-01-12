from ..repository import Repository
from pymongo.collection import Collection
from pydantic import BaseModel

class MongoDBORM(Repository):
    """
    The parent class that performs general CRUD operations on MongoDB in the given repository.
    """

    def __init__(self, repository: Collection) -> None:
        super().__init__(repository)

    def insert(self, schema: BaseModel) -> dict:
        """
        Inserts a schema into the given <self._repository>.
        """
        pass

    def get(self, filter: dict) -> dict:
        """
        Retrieves a schema from <self._repository> with the applied filter.
        """
        pass

    def get_all(self, filter: dict) -> dict:
        """
        Retrieves all schemas from <self._repository> with the applied filter.
        """
        pass

    def delete(self, filter: dict) -> dict:
        """
        Deletes a schema from <self._repository> with the applied filter.
        """
        pass

    def update(self, filter: dict) -> dict:
        """
        Updates a schema from <self._repository> with the applied filter.
        """
        pass