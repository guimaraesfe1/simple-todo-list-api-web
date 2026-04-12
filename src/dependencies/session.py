from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from src.database.engine import engine


def get_session():
    with Session(engine) as s:
        yield s


GetSession = Annotated[Session, Depends(get_session)]
