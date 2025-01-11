from repository import Repository
from typing import Any

class MongoDBORM(Repository):
    def __init__(self, repository: Any):
        super().__init__(repository)