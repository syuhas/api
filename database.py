from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configs import Config
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from contextlib import asynccontextmanager
from typing import AsyncGenerator
import aiomysql

db = Config.SQLALCHEMY_DATABASE_URI

engine = create_async_engine("mysql+aiomysql://syuhas:funstuff@mydb.cypnvtxsedui.us-east-1.rds.amazonaws.com:3306/userdb", echo=True)


async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession
)

@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()




