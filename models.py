from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, LargeBinary
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'
    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    address: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    public_key: Mapped[str] = mapped_column(LargeBinary(300), unique=True, nullable=False)
    # created_at: Mapped[datetime] = mapped_column(DataTime(timezone=True), server_default=func.now())