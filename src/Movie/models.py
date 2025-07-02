from sqlalchemy import Column,Date,DateTime,Enum,Integer,String,ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship

from .enums import Genre,Rating
from ..database import Base

class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String,unique = True)
    year_released = Column()
    cast = Column(list)
    


class Director(Base):

    __tablename__ = "director"

    id = Column(Integer,primary_key=True,index=True)


class Cast(Base):
    
    __tablename__ = "cast"

    id = Column(Integer, primary_key=True,index=True)

