from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func

from entity.base import Base


class GramAltin(Base):
    __tablename__ = "gram_altin"

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String)
    created_date = Column(DateTime(timezone=True), default=func.now())

    def __int__(self, value):
        self.value = value
