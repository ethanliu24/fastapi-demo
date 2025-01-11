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
    def create(self, schema: Any):
        pass

    @abstractmethod
    def get(self, filter: dict):
        pass

    @abstractmethod
    def get_all(self, filter: dict):
        pass

    @abstractmethod
    def delete(self, filter: dict):
        pass

    @abstractmethod
    def update(self, filter: dict):
        pass
