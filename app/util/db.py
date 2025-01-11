"""
For dependency injection for database.
"""
from database.database import Database
from database.mongodb import MongoDB
from settings import ENVIORNMENT

def get_database() -> Database:
    # Might use different database or clustors on development, production or testing
    if ENVIORNMENT == "development":
        return MongoDB()
    return MongoDB()
