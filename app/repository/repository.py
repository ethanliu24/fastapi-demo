from abc import ABC, abstractmethod
from typing import Any

class Repository(ABC):
    """
    Base abstract ORM for crud operations.
    """

    _repository: Any

    def __init__(self, repository: Any):
        self._repository = repository

    @abstractmethod
    def insert(self, schema: Any):
        """
        Inserts a schema into the given <self._repository>.
        """
        pass

    @abstractmethod
    def get(self, filter: dict):
        """
        Retrieves a schema from <self._repository> with the applied filter.
        """
        pass

    @abstractmethod
    def get_all(self, filter: dict):
        """
        Retrieves all schemas from <self._repository> with the applied filter.
        """
        pass

    @abstractmethod
    def delete(self, filter: dict):
        """
        Deletes a schema from <self._repository> with the applied filter.
        """
        pass

    @abstractmethod
    def update(self, filter: dict):
        """
        Updates a schema from <self._repository> with the applied filter.
        """
        pass
