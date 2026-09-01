from datetime import datetime
from pydantic import BaseModel


class ComentarioCreate(BaseModel):
    conteudo: str


class ComentarioResponse(BaseModel):
    id: int
    conteudo: str
    data_criacao: datetime
    id_usuario: int
    id_chamado: int

    class Config:
        from_attributes = True