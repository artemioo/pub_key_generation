

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

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("address", String, nullable=False),
    Column("public_key", String, nullable=False),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
)