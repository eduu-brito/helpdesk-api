from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  relationship
from .base import Base

class User(Base):
    __tablename__ = "usuarios"
    id = Column (Integer, primary_key=True) 
    nome = Column (String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)
    tipo = Column (String(50), nullable=False)

    chamados_abertos = relationship(
        "Chamado",
        foreign_keys="Chamado.id_usuario",
        back_populates="usuario"
    )

    chamados_atendidos = relationship(
        "Chamado",
        foreign_keys="Chamado.id_tecnico",
        back_populates="tecnico"
    )