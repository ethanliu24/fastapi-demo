from .db_manager import DBManager
from pymongo import MongoClient
from pymongo.database import Database as MongoDatabase
from ..config.settings import MONGO_DB_CONNECTION_STRING, DEMO_DB

class MongoDB(DBManager):
    """
    A repository class for MongoDB.
    """

    _client: MongoClient
    _cluster: MongoDatabase

    def __init__(self):
        self.connect()

    def connect(self) -> None:
        """ Makes connection to MongoDB atlas. """
        self._client = MongoClient(MONGO_DB_CONNECTION_STRING)
        self._demo_db = self._client[DEMO_DB]
        print("Connected to MongoDB!")

    def disconnect(self) -> None:
        """ Close the MongoDB connection. """
        self._client.close()

    def get_collection(self, collection_name: str):
        return self._demo_db[collection_name]
