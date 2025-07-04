from fastapi import FastAPI
from .database import Base, engine
from .api import router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Binge Watch Movie API",
    description="Engine Behind Movie API developed in 2025",
    version="1.O",
)

#includes the router defined for the different folder
app.include_router(router)


#import cors middleware
from fastapi.middleware.cors import CORSMiddleware

#allowed origins
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
