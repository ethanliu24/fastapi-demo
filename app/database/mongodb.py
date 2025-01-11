from database.database import Database
from pymongo import MongoClient
from pymongo.database import Database as MongoDatabase
from config.settings import MONGO_DB_CONNECTION_STRING, DEMO_CLUSTER

class MongoDB(Database):
    """
    A repository class for MongoDB.
    """

    _client: MongoClient
    _demo_cluster: MongoDatabase

    def __init__(self):
      self.connect()

    def connect(self) -> None:
      """ Makes connection to MongoDB atlas. """
      self._client = MongoClient(MONGO_DB_CONNECTION_STRING)
      self._demo_cluster = self._client[DEMO_CLUSTER]
      print("Connected to MongoDB!")

    def disconnect(self) -> None:
      """ Close the MongoDB connection. """
      self._client.close()

    def get_collection(self, collection_name: str):
       return self._demo_cluster[collection_name]
