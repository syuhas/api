from fastapi import FastAPI
from sqlalchemy import create_engine


app = FastAPI()

@app.get("/listusers")
async def listusers():
    engine = create_engine()
