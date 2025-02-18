import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '..', '.env')
loaded = load_dotenv(override=True)
print(f".env loaded: {loaded}")

ENVIORNMENT = os.environ.get("ENVIORNMENT")

DOMAIN_URL = os.environ.get("DOMAIN_URL")

MONGO_DB_CONNECTION_STRING = os.environ.get("MONGO_DB_CONNECTION_STRING")
DEMO_DB = "Demo"
USER_COLLECTION = "users"
