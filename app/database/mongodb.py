from database.database import Database
from pymongo import MongoClient
from pymongo.database import Database as MongoDatabase
from settings import MONGO_DB_CONNECTION_STRING, DEMO_CLUSTER

class MongoDB(Database):
    """
    A repository class for MongoDB.
    """

    client: MongoClient
    demo_cluster: MongoDatabase

    def __init__(self):
      self.connect()

    def connect(self) -> None:
      """ Makes connection to MongoDB atlas. """
      self.client = MongoClient(MONGO_DB_CONNECTION_STRING)
      self.demo_cluster = self.client[DEMO_CLUSTER]
      print("Connected to MongoDB!")

    def disconnect(self) -> None:
      """ Close the MongoDB connection. """
      self.client.close()

    def get_collection(self, collection_name: str):
       return self.demo_cluster[collection_name]
