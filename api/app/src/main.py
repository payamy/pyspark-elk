from fastapi import FastAPI
from .routers import search, user
from .database import engine
from . import models


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/user")
app.include_router(search.router, prefix="/search")
