from contextlib import asynccontextmanager

from fastapi import FastAPI

import src.models
from src.database.engine import engine
from src.models.base import Base


@asynccontextmanager
async def lifespan_db(app: FastAPI):
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)
