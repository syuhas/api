from fastapi import FastAPI
from schemas.pydantic_schema import UserBase
from database import get_session
from sqlalchemy import select, and_, or_
import strawberry
from strawberry.fastapi import GraphQLRouter
from schemas.strawberry_schema import Query, Mutation
from models.model import User
from fastapi import Depends


schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()

graphql_app = GraphQLRouter(schema=schema, graphiql=True)


app.include_router(graphql_app, prefix="/graphql")

@app.get("/listusers")
async def listusers():
    async with get_session() as session:
        sql = select(User)
        users = (await session.execute(sql)).scalars().all()
    return users
    
# get user by entering any single or number of fields to filter the query
@app.get("/getuser")
async def getuser(query: UserBase = Depends()):
    filter = []
    values = []
    for key, value in UserBase.model_dump(query).items():
        if value is not None:
            filter.append(getattr(User, key))
            values.append(value)
    filter_dict = dict(zip(filter, values))
    async with get_session() as session:
        sql = select(User).where(or_(f == v for f, v in filter_dict.items()))
        user = (await session.execute(sql)).scalars().all()
    return user



