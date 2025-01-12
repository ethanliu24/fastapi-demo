from ..repository import Repository
from pymongo.collection import Collection
from schema.user import User

class MongoDBORM(Repository):
    def __init__(self, repository: Collection):
        super().__init__(repository)

    def insert(self, user: User):
        """
        Inserts a schema into the given <self._repository>.
        """
        pass

    def get(self, filter: dict):
        """
        Retrieves a schema from <self._repository> with the applied filter.
        """
        pass

    def get_all(self, filter: dict):
        """
        Retrieves all schemas from <self._repository> with the applied filter.
        """
        pass

    def delete(self, filter: dict):
        """
        Deletes a schema from <self._repository> with the applied filter.
        """
        pass

    def update(self, filter: dict):
        """
        Updates a schema from <self._repository> with the applied filter.
        """
        pass