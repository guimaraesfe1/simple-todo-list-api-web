from pydantic import BaseModel


class BaseUserSchema(BaseModel):
    id: int
    name: str
    email: str
    password: str


class SignUpUserSchema(BaseModel):
    name: str
    email: str
    password: str
