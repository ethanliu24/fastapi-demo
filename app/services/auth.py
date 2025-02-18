from ..services.user import UserServices
from ..models.authentication import StandardUserSignUp, JWTToken
from ..models.user import User
from datetime import timedelta, datetime, timezone
import jwt
from ..config.settings import ACCESS_TOKEN_EXPIRE_MINUTES, JWT_SECRET_KEY, JWT_HASH_ALORITHM

class AuthenticationServices:
    _user_services: UserServices

    def __init__(self, user_services: UserServices):
        self._user_services = user_services

    def generate_token(self, data: dict, expires_delta: timedelta | None = None) -> JWTToken:
        encode = data.copy()
        expire = datetime.now(timezone.utc) + \
            (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        encode.update({"exp": expire})
        encoded_jwt = jwt.encode(encode, JWT_SECRET_KEY, algorithm=JWT_HASH_ALORITHM)
        return encoded_jwt

    async def current_user(self) -> User:
        pass

    async def signup(self, user_data: StandardUserSignUp) -> JWTToken:
        user = self._user_services.create_user(user_data)
        token = self.generate_token(data={"sub": user.username})
        return JWTToken(access_token=token, token_type="bearer")

    async def authenticate_user(self) -> User | None:
        # user = self._user_services.get_user()
        pass