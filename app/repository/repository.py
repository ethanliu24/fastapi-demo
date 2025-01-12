from abc import ABC, abstractmethod
from pydantic import BaseModel

class Repository(ABC):
    """
    Base abstract ORM for crud operations.
    """

    @abstractmethod
    def insert(self, schema: BaseModel) -> None:
        """
        Inserts a schema into the given <self._repository>.
        """
        pass

    @abstractmethod
    def get(self, filter: dict) -> dict:
        """
        Retrieves a schema from <self._repository> with the applied filter.
        """
        pass

    @abstractmethod
    def get_all(self, filter: dict) -> list[dict]:
        """
        Retrieves all schemas from <self._repository> with the applied filter.
        """
        pass

    @abstractmethod
    def delete(self, filter: dict) -> dict:
        """
        Deletes a schema from <self._repository> with the applied filter.
        """
        pass

    @abstractmethod
    def update(self, filter: dict) -> dict:
        """
        Updates a schema from <self._repository> with the applied filter.
        """
        pass
