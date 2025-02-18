import os
from os.path import join, dirname
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

dotenv_path = join(dirname(__file__), '..', '.env')
loaded = load_dotenv(override=True)
print(f".env loaded: {loaded}")

ENVIORNMENT = os.environ.get("ENVIORNMENT")

DOMAIN_URL = os.environ.get("DOMAIN_URL")

MONGO_DB_CONNECTION_STRING = os.environ.get("MONGO_DB_CONNECTION_STRING")
DEMO_DB = "Demo"
USER_COLLECTION = "users"

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
pw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
JWT_HASH_ALORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
