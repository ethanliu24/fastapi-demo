from fastapi import FastAPI
from .api.v1 import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root():
    return "Hello World!"