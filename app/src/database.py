from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.src.config import settings


# Создание асинхронного движка SQLAlchemy и создание фабрики сессий из него

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg
)

async_session_factory = async_sessionmaker(async_engine)
