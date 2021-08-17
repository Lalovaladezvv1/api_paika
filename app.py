from fastapi import FastAPI
from routes.room import room

app = FastAPI(title="PAIKA API",version="v0.1")

app.include_router(room)

