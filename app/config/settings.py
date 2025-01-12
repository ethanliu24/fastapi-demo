import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../..', '.env')
load_dotenv(dotenv_path)

ENVIORNMENT = os.environ.get("ENVIORNMENT")

MONGO_DB_CONNECTION_STRING = os.environ.get("MONGO_DB_CONNECTION_STRING")
DEMO_DB = "Demo"
USER_COLLECTION = "users"
