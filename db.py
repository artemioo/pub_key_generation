import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, DeclarativeBase, declared_attr, Mapped, mapped_column
from typing import Generator
from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#
# from datetime import datetime
# from typing import AsyncGenerator
#
# from fastapi import Depends
#
# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
# from sqlalchemy.orm import sessionmaker
#
# from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
#
# DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# Base: DeclarativeMeta = declarative_base()
#
# engine = create_async_engine(DATABASE_URL)
# async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
#
#
# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session
