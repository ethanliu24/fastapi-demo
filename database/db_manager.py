from abc import ABC, abstractmethod

class DBManager(ABC):
    """
    Abstract class to standardize databases.
    """

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get_collection(self, collection_name: str):
        pass
