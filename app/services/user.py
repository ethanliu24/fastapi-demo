from datetime import datetime
from ..repositories.repository import Repository
from ..models.user import User
from ..models.authentication import StandardUserSignUp
from ..utils.utils import generate_id

class UserServices:
    """
    Services for User
    """

    _user_repository: Repository

    def __init__(self, user_repository: Repository):
        self._user_repository = user_repository

    def get_user(self, user_id: str) -> User:
        id = { "id": user_id }
        if not self._user_repository.exists(id):
            raise ValueError("Invalid user ID")

        user = self._user_repository.get(id)
        return User(**user)

    def get_all_users(self, age: int | None, min_age: int | None, max_age: int | None) -> list[User]:
        # This implementation is mongodb specific, may need to redesign or redo if using another db
        # will move this once there's an interface made for user repo
        age_query = {}
        if age is not None: age_query.update({"$eq": age})
        if min_age is not None: age_query.update({"$gte": min_age})
        if max_age is not None: age_query.update({"$lte": max_age})

        filter = {}
        if age_query: filter.update({"age": age_query})

        user_datas = self._user_repository.get_all(filter)
        return [User(**data) for data in user_datas]

    def create_user(self, user_data: StandardUserSignUp) -> User:
        if self._user_repository.exists({ "email": user_data.email }):
            raise ValueError("User with this email exists. Please use another one.")

        creation_time = datetime.now()
        user = User(
            id = generate_id(),
            email = user_data.email,
            username = user_data.username,
            password = user_data.password,
            age = user_data.age,
            created_at = creation_time,
            modified_at = creation_time
        )

        self._user_repository.insert(user)
        return user
