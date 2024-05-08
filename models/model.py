from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base




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


    def as_dict(self):
        return{
            "id": self.id,
            "username": self.username,
            "pw": self.pw,
            "email": self.email,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "phone": self.phone,
            "linkedin": self.linkedin,
            "confirmed": self.confirmed,
            "profile_link": self.profile_link,
            "date_created": self.date_created
        }
