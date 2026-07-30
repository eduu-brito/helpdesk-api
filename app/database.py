from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from app.models.base import Base
from app.models import User, Chamado, Categoria
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"


engine = create_engine(DATABASE_URL)
 
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)