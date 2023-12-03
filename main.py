from fastapi import FastAPI
from database import Session
from models import User, UserBase, DogSchema
from pydantic import BaseModel
from dynamomodel import Dog
import boto3

dogs = Dog()

app = FastAPI()

@app.get("/listusers")
async def listusers():
    session = Session()
    users = session.query(User).all()
    session.close()
    return users
    
@app.get("/getuser/{user_id}")
async def getuser(user_id: int):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    session.close()
    return user

@app.post("/createuser")
async def createuser(user: UserBase):
    session = Session()
    new_user = User(**user.dict())
    session.add(new_user)
    session.commit()
    session.close()
    return new_user


@app.post("/newdog")
async def newdog(dog: DogSchema):
    new_dog = dogs.createdog(dog.dict())
    return new_dog

@app.get("/listdogs")
async def listdogs():
    return dogs.listdogs()

@app.get("/getdog/{dog_name}")
async def getdog(dog_name: str):
    try:
        return dogs.getdog(dog_name)
    except:
        return {"error": "dog not found"}
    
@app.delete("/deletedog/{dog_name}")
async def deletedog(dog_name: str):
    try:
        return dogs.deletedog(dog_name)
    except:
        return {"error": "dog not found"}