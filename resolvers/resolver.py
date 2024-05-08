from sqlalchemy import select, and_, or_, not_, func, desc, asc, update, delete, insert, exists, text, bindparam, ForeignKey, Table, Column, Integer, String, MetaData, create_engine
from fastapi import Depends
from models.model import User
from database import get_session
from schemas.pydantic_schema import UserBase
from scalars.user_scalar import StrawberryUserMutation






async def listusers():
    async with get_session() as session:
        sql = select(User).order_by(User.username)
        users = (await session.execute(sql)).scalars().all()
    return users

async def newUser(
        username: str,
        pw: str = None,
        email: str = None,
        firstname: str = None,
        lastname: str = None,
        phone: str = None,
        linkedin: str = None,
        confirmed: bool = None,
        profile_link: str = None,
        date_created: str = None
    ):
    async with get_session() as session:
        sql = insert(User).values(
            username=username,
            pw=pw,
            email=email,
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            linkedin=linkedin,
            confirmed=confirmed,
            profile_link=profile_link,
            date_created=date_created
        )
        await session.execute(sql)
        query = select(User).filter(User.username == username)
        db_user = (await session.execute(query)).scalars().unique().one()
        await session.commit()
    return db_user