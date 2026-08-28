from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.chamado import ChamadoCreate, ChamadoResponse
from app.database import get_db
from app.models.chamado import Chamado
from app.security import verificar_token, verificar_tecnico

router = APIRouter()


@router.post("/chamados", response_model=ChamadoResponse)
def criar_chamado(
    chamado: ChamadoCreate,
    db=Depends(get_db),
    usuario_token=Depends(verificar_token)
):
    novo_chamado = Chamado(
        titulo=chamado.titulo,
        descricao=chamado.descricao,
        prioridade=chamado.prioridade,
        status="aberto",
        data_criacao=datetime.now(timezone.utc),
        id_usuario=int(usuario_token["sub"]),
        id_categoria=chamado.id_categoria
    )

    db.add(novo_chamado)
    db.commit()
    db.refresh(novo_chamado)

    return novo_chamado

@router.get("/chamados", response_model=list[ChamadoResponse])
def listar_chamados(
    db=Depends(get_db),
    usuario_token = Depends(verificar_token)
):
    chamados = db.query(Chamado).filter(
        Chamado.id_usuario == int(usuario_token["sub"])
    ).all()

    return chamados

@router.get("/chamados/{id}", response_model=ChamadoResponse)
def buscar_chamado(
    id: int,
    db=Depends(get_db),
    usuario_token=Depends(verificar_token)
):
    chamado = db.query(Chamado).filter(
        Chamado.id == id
    ).first()

    if chamado is None:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )

    if chamado.id_usuario != int(usuario_token["sub"]):
        raise HTTPException(
            status_code=403,
            detail="Você não tem acesso a este chamado"
        )

    return chamado

@router.put("/chamados/{id}/assumir", response_model=ChamadoResponse)
def assumir_chamado(
    id: int,
    db=Depends(get_db),
    tecnico_token=Depends(verificar_tecnico)
):
    chamado = db.query(Chamado).filter(
        Chamado.id == id
    ).first()

    if chamado is None:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )

    if chamado.id_tecnico is not None:
        raise HTTPException(
            status_code=400,
            detail="Este chamado já foi assumido por um técnico"
        )

    chamado.id_tecnico = int(tecnico_token["sub"])
    chamado.status = "em_atendimento"

    db.commit()
    db.refresh(chamado)

    return chamado

@router.put("/chamados/{id}/fechar", response_model=ChamadoResponse)
def fechar_chamado(
    id: int,
    db=Depends(get_db),
    tecnico_token=Depends(verificar_tecnico)
):
    chamado = db.query(Chamado).filter(
        Chamado.id == id
    ).first()

    if chamado is None:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )

    if chamado.id_tecnico != int(tecnico_token["sub"]):
        raise HTTPException(
            status_code=403,
            detail="Somente o técnico responsável pode fechar este chamado"
        )

    if chamado.status == "fechado":
        raise HTTPException(
            status_code=400,
            detail="Este chamado já está fechado"
        )

    chamado.status = "fechado"
    chamado.data_fechamento = datetime.now(timezone.utc)

    db.commit()
    db.refresh(chamado)

    return chamado