from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

from .enums import Genre, Rating

#  id = Column(Integer, primary_key = True, index = True,autoincrement=True)
#     title = Column(String,unique = True,index = True)
#     description = Column(String)
#     genre = Column(Enum(Genre))
#     year_released = Column()
#     cast = Column(list)
#     runtime = Column(datetime)
#     director_id = Column(Integer,ForeignKey=("Director.id"))

class MovieBase(BaseModel):
    title : str
    description : str
    genre : str
    year_released : int
    cast : list
    runtime : datetime
    director_id : int


# class UserBase(BaseModel):
#     email: str
#     username: str

# class UserCreate(UserBase):
#     password: str


# class UserUpdate(BaseModel):
#     name: Optional[str] = None
#     dob: Optional[date] = None
#     gender: Optional[Gender] = None
#     bio: Optional[str] = None
#     location: Optional[str] = None
#     profile_pic: Optional[str] = None


# class User(UserBase, UserUpdate):
#     id: int
#     created_dt:datetime

#     class Config:
#         from_attributes = True