# For dependency injection for database.

from database.database import Database
from database.mongodb import MongoDB
from repository.repository import Repository
from repository.mongodb import UserRepository as UserRepository
from config.settings import (
    ENVIORNMENT,
    MONGO_DB_CONNECTION_STRING,
    DEMO_CLUSTER,
    USER_COLLECTION
)

class DB:
    """
    Wrapper class for accessing a database.
    Might use different database or clustors on development, production or testing.
    """

    _db: Database
    _user_repository: Repository

    def __init__(self) -> None:
        if ENVIORNMENT == "development":
            self._init_mongodb(MONGO_DB_CONNECTION_STRING, DEMO_CLUSTER)
        elif ENVIORNMENT == "production":
            raise Exception("Production enviornment not supported yet")
        else:
            raise Exception("Test enviornment not supported yet")

    def get_user_repository(self) -> Repository:
        return self._user_repository

    def _init_mongodb(self) -> None:
        mongodb = MongoDB()
        self._db = mongodb
        self._user_repository = UserRepository(mongodb.get_collection(USER_COLLECTION))
