from typing import Optional

from pydantic import BaseModel


class CreateUserSchema(BaseModel):
    title: str
    description: str


class UpdateUserSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]
