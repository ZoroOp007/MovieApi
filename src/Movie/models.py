from sqlalchemy import Column,Date,DateTime,Enum,Integer,String,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
from typing import List

from ..Auth.enums import Gender
from .enums import Genre,Rating
from ..database import Base


#implementing many to many relationship









class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key = True, index = True,autoincrement=True)
    title = Column(String,unique = True,index = True)
    description = Column(String)
    genre = Column(Enum(Genre))
    year_released = Column(Integer)
    runtime = Column(datetime)

    #other useful attributes
    budget = Column(Integer)
    revenue = Column(Integer)
    rating = Column(Enum(Rating))
    language = Column(list)
    country = Column(String)
    poster_url = Column(String)
    trailer_url = Column(String)

    #Cast and Director
    director_id = Column(Integer,ForeignKey=("Director.id"))
    cast = Column(list)

    class config:
        orm_mode = True
    


class Director(Base):

    __tablename__ = "director"

    id = Column(Integer,primary_key=True,index=True,autoincrement=True)
    name = Column(String,index=True)
    gender = Column(Enum(Gender))

    class config:
        orm_mode = True


class Cast(Base):
    
    __tablename__ = "cast"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String , index = True)
    age = Column(Integer)
    gender = Column(Enum(Gender))
    Role = Column(String)
    character_name = Column(String,index=True)
    character_details = Column(String(300))

    movie_id = relationship()

    class config:
        orm_mode = True

