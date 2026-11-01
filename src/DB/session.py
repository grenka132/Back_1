from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine)
from sqlalchemy.orm import DeclarativeBase
from src.config import setting
from typing import AsyncGenerator

engine: AsyncEngine = create_async_engine(url=setting.SQLALCHEMY_DATABASE_URL)
async_session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(bind=engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session