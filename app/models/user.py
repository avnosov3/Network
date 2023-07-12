from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from sqlalchemy import Column, String

from ..core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    nickname = Column(String, nullable=False)
