# For dependency injection for database.

from database.database import Database
from database.mongodb import MongoDB
from repository.repository import Repository
from repository.mongodb import UserRepository as UserRepository
from settings import ENVIORNMENT, USER_COLLECTION

class DB:
    """
    Wrapper class for accessing a database.
    Might use different database or clustors on development, production or testing.
    """

    _db: Database
    _user_repository: Repository

    def __init__(self) -> None:
        # Might use different database or clustors on development, production or testing.
        # if ENVIORNMENT == "development":
        #     pass
        mongodb = MongoDB()
        self._db = mongodb
        self._user_repository = UserRepository(mongodb.get_collection(USER_COLLECTION))

    def get_user_repository(self) -> Repository:
        return self._user_repository
