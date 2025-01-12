from .mongodb_orm import MongoDBORM
from pydantic import BaseModel
from pymongo.collection import Collection

class UserRepository(MongoDBORM):
    def __init__(self, user_repository: Collection) -> None:
        super().__init__(user_repository)

    def insert(self, user: BaseModel) -> None:
        """
        Inserts a schema into the given <self._repository>.

        Precondition:
        - <user>'s email is unique, i.e. not in the database
        """
        super().insert(user)
