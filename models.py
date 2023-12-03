from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import pytz


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    pw = Column(String, nullable=False)
    email = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    phone = Column(String)
    linkedin = Column(String)
    confirmed = Column(Boolean, default=False)
    profile_link = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow, nullable=False)

class UserBase(BaseModel):
    id: int
    username: str
    pw: str
    email: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    confirmed: bool = False
    profile_link: Optional[str] = None
    date_created: datetime = datetime.now(pytz.timezone("US/Eastern"))

class DogSchema(BaseModel):
    name: str
    


    



