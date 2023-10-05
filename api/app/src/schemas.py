import datetime

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    name: str
    signup_timestamp: datetime.datetime


class UserCreate(BaseModel):

    username: str = Field(max_length=20)
    name: str = Field(max_length=20)
    password: str


class VisitCreate(BaseModel):

    endpoint: str
    query: str


class Token(BaseModel):
    access_token: str
    token_type: str
