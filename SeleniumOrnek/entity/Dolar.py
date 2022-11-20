from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

from entity.base import Base


class Dolar(Base):
    __tablename__ = "dolar"

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String)
    created_date = Column(DateTime(timezone=True), default=func.now())

    def __int__(self, value):
        self.value = value
