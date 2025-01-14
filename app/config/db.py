from __future__ import annotations
from ..database.db_manager import DBManager
from ..database.mongodb import MongoDB
from ..repositories.repository import Repository
from ..repositories.mongodb.user_repository import MongoUserRepository
from ..config.settings import (
    ENVIORNMENT,
    USER_COLLECTION
)

class DB:
    """
    Wrapper class for databases. Services in this app will refer to this class to access different
    databases. Might use different database or clustors on development, production or testing.
    """

    _db: DBManager
    _user_repository: Repository

    def __init__(self) -> None:
        if ENVIORNMENT == "development":
            self._init_mongodb()
        elif ENVIORNMENT == "production":
            raise Exception("Production enviornment not supported yet")
        else:
            raise Exception("Test enviornment not supported yet")

    def get_user_repository(self) -> Repository:
        return self._user_repository

    def _init_mongodb(self) -> None:
        mongodb = MongoDB()
        self._db = mongodb

        user_collection = mongodb.get_collection(USER_COLLECTION)
        user_collection.create_index("email", unique=True)
        self._user_repository = MongoUserRepository(user_collection)
