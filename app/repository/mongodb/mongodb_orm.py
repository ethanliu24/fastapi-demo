from repository import Repository
from pymongo.collection import Collection

class MongoDBORM(Repository):
    def __init__(self, repository: Collection):
        super().__init__(repository)