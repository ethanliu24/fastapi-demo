from .mongodb_orm import MongoDBORM
from pymongo.collection import Collection
from ..user_repository import UserRepository
from ...models.user import User

class MongoUserRepository(MongoDBORM, UserRepository):
    def __init__(self, user_repository: Collection) -> None:
        MongoDBORM.__init__(self, user_repository)

    def email_exists(self, email: str) -> bool:
        return super().exists({ "email": email })

    def user_id_exists(self, user_id: str) -> bool:
        return super().exists({ "id": user_id })

    def get_user_by_id(self, user_id: str) -> bool:
        return super().get({ "id": user_id })

    def query_all_users(self, age: int | None, min_age: int | None, max_age: int | None) -> list[User]:
        age_query = {}
        if age is not None: age_query.update({"$eq": age})
        if min_age is not None: age_query.update({"$gte": min_age})
        if max_age is not None: age_query.update({"$lte": max_age})

        filter = {}
        if age_query: filter.update({"age": age_query})

        return self.get_all(filter)

    def update_user(self, user_id: str, new_data: User) -> None:
        # Checkout upsert attribute
        super().update({"id": user_id}, { "$set": new_data.model_dump() })

    def delete_user(self, user_id: str) -> bool:
        # maybe make update user return bool too
        return super().delete({"id": user_id})
