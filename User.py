from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from sqlalchemy.sql import text, select

connection_string = "postgresql://ojerfdbw:s2sK21OrGEeHBSEzJYp5F5qs4otnr_5D@hansken.db.elephantsql.com:5432/ojerfdbw"
db = create_engine(connection_string, echo=True)
base = declarative_base()


class User(base):
    __tablename__ = "user"  # tablo adı

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    year = Column(String)
    job = Column(String)


Session = sessionmaker(db)
sesion = Session()
base.metadata.create_all(db)


def create_user(name: str, surname: str, year: str, job: str):
    docktor_stranger = User(name=name, surname=surname, year=year, job=job)
    sesion.add(docktor_stranger)
    sesion.commit()
    sesion.close()

    return True

def list_users():
    all_users =  sesion.query(User)
    sesion.close()

    return  [u.__dict__ for u in all_users.all()]
