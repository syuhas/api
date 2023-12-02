from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    id: int
    username: str
    pw: str
    email: str
    firstname: str
    lastname: str
    phone: str
    linkedin: str
    confirmed: bool
    profile_link: str
    date_created: datetime

    class Config:
        orm_mode = True

class UserList(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

class UserEmail(BaseModel):
    email: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    pw: str

    class Config:
        orm_mode = True

