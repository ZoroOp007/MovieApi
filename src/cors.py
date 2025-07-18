from fastapi.middleware.cors import CORSMiddleware
from main import app



#allowed origins
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "*",
    "http://localhost:5173/",
    "https://just-watch-frontend.vercel.app/"
]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
