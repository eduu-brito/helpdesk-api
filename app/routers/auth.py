from fastapi import APIRouter, Depends, HTTPException
from app.schemas.auth import UserLogin
from app.database import get_db
from app.models.user import User
from dotenv import load_dotenv
from datetime import datetime, timedelta,timezone
from app.core.config import SECRET_KEY, ALGORITHM
import bcrypt
import jwt
import os


load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


router = APIRouter()

@router.post("/login")
def login(user:UserLogin, db=Depends(get_db)):
    usuario = db.query (User).filter(User.email == user.email).first()
    if usuario is None:
        raise HTTPException(
            status_code=401,
            detail= "Credenciais inválidas"
        )
    if not bcrypt.checkpw(user.senha.encode("utf-8"),usuario.senha.encode ("utf-8")):
        raise HTTPException(
            status_code=401,
            detail="Credenciais inválidas")
    expires = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload = {
    "sub": str(usuario.id),
    "tipo": usuario.tipo,
    "exp": expires

    }
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return {
        "access_token": token,
        "token_type": "bearer"
    }
    

        
