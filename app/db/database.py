from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

#load data from the env file
load_dotenv()

#set this as the URL in the env file
database_url = os.getenv("DATABASE_URL")

#this establishes the engine
engine = create_engine(database_url)

#create the session to communicate to database
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

#create a class base
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()