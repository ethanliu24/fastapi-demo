from mongodb_orm import MongoDBORM
from pymongo.collection import Collection

class UserRepository(MongoDBORM):
    def __init__(self, repository: Collection):
        super().__init__(repository)
        