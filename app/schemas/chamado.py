from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ChamadoCreate(BaseModel):
    titulo: str
    descricao: str
    prioridade: str
    id_categoria: int


class ChamadoResponse(BaseModel):
    model_config = ConfigDict (from_attributes=True)
    id: int
    titulo: str
    descricao: str
    prioridade: str
    status: str
    data_criacao: datetime
    data_fechamento: datetime | None
    id_usuario: int
    id_tecnico: int | None
    id_categoria: int
