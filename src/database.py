from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv
load_dotenv()

#this line is to connect our app with the postgres database
SQLALCHEMY_DATABASE_URL = "postgresql://user:qUzj02TINfCknYHJvVRbOKagWNEiK4jL@dpg-d1itceadbo4c73bmsb0g-a.oregon-postgres.render.com/fastapi_ge19"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()