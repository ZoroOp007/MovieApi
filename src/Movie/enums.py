from enum import Enum

class Genre(Enum,str):
    ACTION = "action"
    COMEDY = "comedy"
    DRAMA  = "drama"
    FANTASY = "fantasy"
    HORROR = "horror"
    MYSTERY = "mystery"
    ROMANCE = "romance"
    THRILLER = "thriller"
    WESTERN = "western"

class Rating(Enum,str):
    U = "unrestricted"
    UA = "unrestricted with parental guidance"
    A = "adult"
    S = "restricted to special class"
    