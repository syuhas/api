import strawberry
from typing import Optional
from pydantic import Field, typing
from models.model import Base
from datetime import datetime

@strawberry.type
class StrawberryUser:
    id: Optional[int]
    username: Optional[str]
    pw: Optional[str]
    email: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
    linkedin: Optional[str]
    confirmed: Optional[bool]
    profile_link: Optional[str]
    date_created: Optional[datetime]

@strawberry.type
class StrawberryUserMutation:
    id: Optional[int]
    username: Optional[str]
    pw: Optional[str]
    email: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
    linkedin: Optional[str]
    confirmed: Optional[bool]
    profile_link: Optional[str]
    date_created: Optional[datetime]

@strawberry.type
class TestQuery:
    id: Optional[int]
    username: Optional[str]
    pw: Optional[str]
    email: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
    linkedin: Optional[str]
    confirmed: Optional[bool]
    profile_link: Optional[str]
    date_created: Optional[datetime]
    
    