from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from config import settings

DATABASE_URL: str = settings.database_url_asyncpg

async_engine = create_async_engine(DATABASE_URL)

async_session_fabric = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)


# DeclarativeBase implementation
class Base(DeclarativeBase):
    pass