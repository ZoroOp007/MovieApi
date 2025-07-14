from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

from .enums import Genre, Rating

class MovieBase(BaseModel):
    title : str
    description : str
    genre : str
    year_released : int
    cast : list
    runtime : datetime
    director_id : int

class UpdateMovie(MovieBase):


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