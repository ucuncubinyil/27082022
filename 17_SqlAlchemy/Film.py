from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from sqlalchemy.sql import text, select

connection_string = "postgresql://ojerfdbw:s2sK21OrGEeHBSEzJYp5F5qs4otnr_5D@hansken.db.elephantsql.com:5432/ojerfdbw"
db = create_engine(connection_string, echo=True)
base = declarative_base()


class Film(base):
    __tablename__ = "films"  # tablo adı

    id          = Column(Integer, autoincrement=True, primary_key=True)
    title       = Column(String)
    director    = Column(String)
    year        = Column(String)


Session = sessionmaker(db)
sesion = Session()
base.metadata.create_all(db)

def  create_film():
    docktor_stranger =  Film(title="Doctor Stranger", director="Scott Derrison", year="2016")
    sesion.add(docktor_stranger)
    sesion.commit()
    sesion.close()

# create_film()

def find_all_films():
    films = sesion.query(Film) #select * from films
    for film in films:
        print(film.id, film.title, film.director, film.year)

    sesion.close()

# find_all_films()


def  find_film_by_id(id:int):
    film =  sesion.query(Film).filter( text("id = :id")).params(id=id).one()
    print(film.title)

# find_film_by_id(1)

def update_film_by_id(id:int):

    global  docktor_stranger
    docktor_stranger =  sesion.query(Film).filter(text("id =:id")).params(id=id).one()
    docktor_stranger.year =  "2019"
    sesion.commit()
    sesion.close()

# update_film_by_id(1)


def  delete_film_by_id(id:int):
    global  docktor_stranger
    docktor_stranger =  sesion.query(Film).filter(text("id =:id")).params(id=id).one()
    sesion.delete(docktor_stranger)
    sesion.commit()
    sesion.close()

delete_film_by_id(1)