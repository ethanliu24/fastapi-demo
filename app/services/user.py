from ..repositories.repository import Repository

class UserServices:
    """
    Services for User
    """

    _user_repository: Repository

    def __init__(self, user_repository: Repository):
        self._user_repository = user_repository

    def hi(self):
        print("hi")