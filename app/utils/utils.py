import uuid
from ..config.settings import DOMAIN_URL

def generate_id() -> str:
    return str(uuid.uuid4())

def create_token_data(user_id: str) -> dict:
    return {
        "sub": user_id,
        "iss": DOMAIN_URL
    }
