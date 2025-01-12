from .mongodb_orm import MongoDBORM
from pydantic import BaseModel
from pymongo.collection import Collection
from pymongo.errors import DuplicateKeyError

class UserRepository(MongoDBORM):
    def __init__(self, user_repository: Collection) -> None:
        super().__init__(user_repository)

    def insert(self, user: BaseModel) -> None:
        """
        Inserts a data_model into the given <self._repository>.

        Precondition:
        - <user>'s email is unique, i.e. not in the database
        """
        try:
            super().insert(user)
        except DuplicateKeyError:
            raise ValueError("User with this email exists. Please use another one.")