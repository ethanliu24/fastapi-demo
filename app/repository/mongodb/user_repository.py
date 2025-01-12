from .mongodb_orm import MongoDBORM
from pydantic import BaseModel
from pymongo.collection import Collection

class UserRepository(MongoDBORM):
    def __init__(self, repository: Collection) -> None:
        super().__init__(repository)

    def insert(self, user: BaseModel) -> dict:
        super().insert(user)
