from ..services.user import UserServices
from ..models.authentication import StandardUserSignUp, StandardUserLogin, JWTToken
from ..models.user import User
from datetime import timedelta, datetime, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from ..config.settings import ACCESS_TOKEN_EXPIRE_MINUTES, JWT_SECRET_KEY, JWT_HASH_ALORITHM, pw_context

class AuthenticationServices:
    _user_services: UserServices

    def __init__(self, user_services: UserServices):
        self._user_services = user_services

    def generate_token(self, data: dict, expires_delta: timedelta | None = None, type: str = "bearer") -> JWTToken:
        encode = data.copy()
        expire = datetime.now(timezone.utc) + \
            (expires_delta if expires_delta else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        encode.update({"exp": expire})
        encoded_jwt = jwt.encode(encode, JWT_SECRET_KEY, algorithm=JWT_HASH_ALORITHM)
        return JWTToken(access_token=encoded_jwt, token_type=type)

    async def get_current_user(self, token: str) -> User:
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_HASH_ALORITHM])
            user_id = payload.get("sub")
            if not user_id:
                return None
        except InvalidTokenError:
            return None

        try:
            return await self._user_services.get_user(user_id)
        except ValueError:
            return None

    async def signup(self, user_data: StandardUserSignUp) -> JWTToken:
        user = await self._user_services.create_user(user_data)
        token = self.generate_token(data={"sub": user.id})
        return token

    async def authenticate_user(self, login_data: StandardUserLogin) -> User | None:
        try:
            user = await self._user_services.get_user_by_email(login_data.email)
            if not self._verify_password(login_data.password, user):
                return None
            return user
        except ValueError:
            return None

    def _verify_password(self, pwd: str, user: User) -> bool:
        return pw_context.hash(pwd) == user.password
