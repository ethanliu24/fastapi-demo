from fastapi import FastAPI
from .config.routes import api_router_v1
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(api_router_v1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
