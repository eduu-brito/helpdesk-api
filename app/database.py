from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

DATABASE_URL = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

print(f"Usuário: '{user}'")
print(f"Host: '{host}'")
print(f"Porta: '{port}'")
print(f"Banco: '{database}'")





engine = create_engine(DATABASE_URL)
 
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal ()
    try:
        yield db
    finally:
        db.close()
        
try:
    with engine.connect() as connection:
        print("✅ Conexão com o banco realizada com sucesso!")
except Exception as e:
    print(f"❌ Erro ao conectar: {e}")