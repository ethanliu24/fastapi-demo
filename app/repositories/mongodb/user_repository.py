from .mongodb_orm import MongoDBORM
from pymongo.collection import Collection

class UserRepository(MongoDBORM):
    def __init__(self, user_repository: Collection) -> None:
        super().__init__(user_repository)
