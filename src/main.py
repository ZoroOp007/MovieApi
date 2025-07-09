from fastapi import FastAPI
from .database import Base, engine
from .api import router


Base.metadata.create_all(bind=engine)



app = FastAPI(
    title="Binge Watch Movie API",
    description="Engine Behind Movie API developed in 2025",
    version="1.O",
)

@app.get("/")
async def read_item():

    message = {
        "title" : app.version,
        "description" : app.description,
        "version" : app.version,
        "greet" : "Hello, this is movie api developed by Badal to serve the purpose of building a backend service for modern Movie app"
    }
    return message

    

#includes the router defined for the different folder
app.include_router(router)
