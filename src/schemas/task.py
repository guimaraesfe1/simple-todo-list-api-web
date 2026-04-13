from typing import Optional

from pydantic import BaseModel


class BaseTaskSchema(BaseModel):
    id: int
    title: Optional[str]
    description: Optional[str]
    user_id: int


class CreateUserSchema(BaseModel):
    title: str
    description: str


class UpdateUserSchema(BaseModel):
    title: Optional[str]
    description: Optional[str]
