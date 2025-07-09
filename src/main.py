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
        "greet" : "Hello, this is movie api developed by Badal and Deepak to serve our movie app which allows user to binge watch the movie along with their friends. It allows real-time chatting to feel the presence on one another even after being at distance."
    }
    
    return message

    

#includes the router defined for the different folder
app.include_router(router)
