from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://txhjnzfz:POG3Xkvdr6Y-QzaBo64NOTHdJHto8isl@tiny.db.elephantsql.com/txhjnzfz")
_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()