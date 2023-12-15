

"""
я ввожу адрес
если есть совпадение - возврат публ ключа из бд
если нет - генерация для этого адреса ключа, сохранение в бд, и возврат

юзер
адресс
публ ключ
дата добавления

"""

from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

# metadata = MetaData()
#
# user = Table(
#     "user",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("address", String, nullable=False),
#     Column("public_key", String, nullable=False),
#     Column("created_at", TIMESTAMP, default=datetime.utcnow),
# )

class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'
    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    address: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    public_key: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)
    # created_at: Mapped[datetime] = mapped_column(DataTime(timezone=True), server_default=func.now())