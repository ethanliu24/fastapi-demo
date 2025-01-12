from abc import ABC, abstractmethod
from pydantic import BaseModel

class Repository(ABC):
    """
    Base abstract ORM for crud operations.
    """

    @abstractmethod
    def insert(self, model: BaseModel) -> None:
        """
        Inserts a data_model into the given <self._repository>.
        """
        pass

    @abstractmethod
    def get(self, filter: dict) -> dict:
        """
        Retrieves a data_model from <self._repository> with the applied filter.
        """
        pass

    @abstractmethod
    def get_all(self, filter: dict) -> list[dict]:
        """
        Retrieves all data_models from <self._repository> with the applied filter.
        """
        pass

    @abstractmethod
    def delete(self, filter: dict) -> dict:
        """
        Deletes a data_model from <self._repository> with the applied filter.
        """
        pass

    @abstractmethod
    def update(self, filter: dict) -> dict:
        """
        Updates a data_model from <self._repository> with the applied filter.
        """
        pass

    @abstractmethod
    def exists(self, query: dict) -> bool:
        """
        Check if a model exists in <self._repository> using the given filter.
        """
        pass
