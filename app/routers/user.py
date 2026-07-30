import bcrypt
from app.schemas.user import UserCreate, UserResponse
from app.database import get_db
from app.models.user import User
from fastapi import APIRouter, Depends

router = APIRouter()

@router.post("/usuarios", response_model=UserResponse)
def criar_usuario(user: UserCreate, db = Depends (get_db)):
    senha_hash = bcrypt.hashpw(user.senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    novo_usuario = User(
    nome=user.nome,
    email=user.email,
    senha=senha_hash,
    tipo=user.tipo
)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario
