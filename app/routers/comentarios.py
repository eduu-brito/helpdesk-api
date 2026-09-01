from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException

from app.database import get_db
from app.models.chamado import Chamado
from app.models.comentario import Comentario
from app.schemas.comentario import ComentarioCreate, ComentarioResponse
from app.security import verificar_token


router = APIRouter()


@router.post(
    "/chamados/{id}/comentarios",
    response_model=ComentarioResponse
)
@router.post(
    "/chamados/{id}/comentarios",
    response_model=ComentarioResponse
)
def criar_comentario(
    id: int,
    comentario: ComentarioCreate,
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

    usuario_id = int(usuario_token["sub"])
    tipo_usuario = usuario_token["tipo"]

    # Admin pode comentar em qualquer chamado
    if tipo_usuario == "admin":
        pass

    # Dono do chamado pode comentar
    elif chamado.id_usuario == usuario_id:
        pass

    # Técnico responsável pode comentar
    elif chamado.id_tecnico == usuario_id:
        pass

    # Outros usuários não podem comentar
    else:
        raise HTTPException(
            status_code=403,
            detail="Você não tem permissão para comentar neste chamado"
        )

    novo_comentario = Comentario(
        conteudo=comentario.conteudo,
        data_criacao=datetime.now(timezone.utc),
        id_usuario=usuario_id,
        id_chamado=chamado.id
    )

    db.add(novo_comentario)
    db.commit()
    db.refresh(novo_comentario)

    return novo_comentario
@router.get(
    "/chamados/{id}/comentarios",
    response_model=list[ComentarioResponse]
)
def listar_comentarios(
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

    usuario_id = int(usuario_token["sub"])
    tipo_usuario = usuario_token["tipo"]

    # Admin pode visualizar qualquer chamado
    if tipo_usuario == "admin":
        pass

    # Dono do chamado pode visualizar
    elif chamado.id_usuario == usuario_id:
        pass

    # Técnico responsável pode visualizar
    elif chamado.id_tecnico == usuario_id:
        pass

    # Qualquer outro usuário é bloqueado
    else:
        raise HTTPException(
            status_code=403,
            detail="Você não tem permissão para visualizar os comentários deste chamado"
        )

    comentarios = db.query(Comentario).filter(
        Comentario.id_chamado == id
    ).all()

    return comentarios