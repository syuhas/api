from typing import Optional
from pydantic import BaseModel
import pytz
from datetime import datetime



class UserBase(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None
    pw: Optional[str] = None
    email: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    confirmed: Optional[bool] = None
    profile_link: Optional[str] = None
    date_created: Optional[datetime] = None


class CreateUser(BaseModel):
    username: str
    email: str
    date_created: datetime = datetime.now(pytz.timezone("US/Eastern"))

class GetUserBase(BaseModel):
    id: Optional[int] = None
    username: Optional[str] = None