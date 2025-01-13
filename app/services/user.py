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
