from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

if settings.MODE == "TEST":
    DATABASE_URL = settings.TEST_DB_URI
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = settings.DB_URI
    DATABASE_PARAMS = {}


async_engine = create_async_engine(DATABASE_URL, echo=False, **DATABASE_PARAMS)
async_session_maker = async_sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
