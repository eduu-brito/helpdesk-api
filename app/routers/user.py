import bcrypt
from app.schemas.user import UserCreate, UserResponse
from app.database import get_db
from app.models.user import User
from fastapi import APIRouter, Depends
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.get("/usuarios", response_model=list[UserResponse])
def listar_usuarios(db=Depends(get_db)):
    usuarios=db.query(User).all()
    return usuarios


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


@router.get("/usuarios/{id}", response_model=UserResponse)
def buscar_usuario(id: int, db=Depends(get_db)):
    usuario = db.query(User).filter(User.id == id).first()
    if usuario == None:
        raise HTTPException(
            status_code=404,
            detail= "Usuário não encontrado"
        )
    else:
        return usuario

@router.put("/usuarios/{id}", response_model=UserResponse)
def atualizar_usuario(id:int,user: UserCreate, db=Depends(get_db)):
    usuario = db.query(User).filter(User.id == id).first()
    if usuario == None:
            raise HTTPException(
                status_code=404,
                detail= "Usuario não encontrado."
            )  
      
    usuario.nome = user.nome
    usuario.email = user.email
    usuario.tipo = user.tipo
    senha_hash = bcrypt.hashpw(user.senha.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    usuario.senha = senha_hash
    db.commit ()
    db.refresh (usuario)

    return usuario

@router.delete ("/usuarios/{id}")
def deletar_usuario(id: int, db=Depends(get_db)):
     usuario = db.query (User).filter(User.id == id).first()
     if usuario == None:
        raise HTTPException(
            status_code=404,
            detail="Usuario não encontrado"
        )
     db.delete(usuario)
     db.commit()
     return {"message": "Usuário deletado com sucesso"}
     

@router.get("/usuarios/email/{email}",response_model=UserResponse)
def buscar_usuario_email (email: str, db=Depends(get_db)):
    usuario = db.query (User).filter(User.email == email).first()
    if usuario == None:
        raise HTTPException(
            status_code=404,
            detail="Email não encontrado"
        )
    return usuario


