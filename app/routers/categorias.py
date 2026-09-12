from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.models.categorias import Categoria
from app.security import verificar_token
from pydantic import BaseModel
from app.security import verificar_token, verificar_admin
router = APIRouter()

class CategoriaCreate(BaseModel):
    nome: str


@router.post("/categorias")
def criar_categoria(
    categoria: CategoriaCreate,
    db=Depends(get_db),
    _admin=Depends(verificar_admin)
):
    nova_categoria = Categoria(
        nome=categoria.nome
    )

    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)

    return nova_categoria

@router.get("/categorias")
def listar_categorias(
    db=Depends(get_db),
    usuario_token=Depends(verificar_token)
):
    categorias = db.query(Categoria).all()

    return categorias

@router.get("/categorias/{id}")
def buscar_categoria(
    id: int,
    db=Depends(get_db),
    usuario_token=Depends(verificar_token)
):
    categoria = db.query(Categoria).filter(
        Categoria.id == id
    ).first()

    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada"
        )

    return categoria

@router.put("/categorias/{id}")
def atualizar_categoria(
    id: int,
    categoria: CategoriaCreate,
    db=Depends(get_db),
    _admin=Depends(verificar_admin)
):
    categoria_db = db.query(Categoria).filter(Categoria.id == id).first()

    if categoria_db is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada"
        )

    categoria_db.nome = categoria.nome

    db.commit()
    db.refresh(categoria_db)

    return categoria_db

@router.delete("/categorias/{id}")
def deletar_categoria(
    id: int,
    db=Depends(get_db),
    _admin=Depends(verificar_admin)
):
    categoria_db = db.query(Categoria).filter(Categoria.id == id).first()

    if categoria_db is None:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada"
        )

    try:
        db.delete(categoria_db)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Não é possível excluir a categoria porque ela está sendo utilizada por um chamado"
        )

    return {"message": "Categoria deletada com sucesso"}