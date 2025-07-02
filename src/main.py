from fastapi import FastAPI
from .database import Base, engine
from .api import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Binge Watch Movie API",
    description="Engine Behind Movie API developed in 2025",
    version="1.O",
)
app.include_router(router)
