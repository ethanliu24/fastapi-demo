from fastapi import FastAPI
from .config.routes import api_router_v1

app = FastAPI()

app.include_router(api_router_v1)
