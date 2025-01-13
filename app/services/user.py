from datetime import datetime
from ..repositories.repository import Repository
from ..repositories.user_repository import UserRepository
from ..models.user import User, UserUpdate
from ..models.authentication import StandardUserSignUp
from ..utils.utils import generate_id
from typing import Union

class UserServices:
    """
    Services for User
    """

    _user_repository: Union[Repository, UserRepository]

    def __init__(self, user_repository: Repository):
        self._user_repository = user_repository

    def get_user(self, user_id: str) -> User:
        if not self._user_repository.user_id_exists(user_id):
            raise ValueError("Invalid user ID")

        user = self._user_repository.get_user_by_id(user_id)
        return User(**user)

    def get_all_users(self, age: int | None, min_age: int | None, max_age: int | None) -> list[User]:
        user_datas = self._user_repository.query_all_users(age, min_age, max_age)
        return [User(**data) for data in user_datas]

    def create_user(self, user_data: StandardUserSignUp) -> User:
        if self._user_repository.email_exists(user_data.email):
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

    def update_user(self, user_id: str, new_data: UserUpdate) -> None:
        user = self.get_user(user_id)

        user.username = new_data.username
        user.password = new_data.password
        user.email = new_data.email
        user.age = new_data.age
        user.modified_at = datetime.now()

        self._user_repository.update_user(user_id, user)
