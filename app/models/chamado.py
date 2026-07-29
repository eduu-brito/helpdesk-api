from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base

class Chamado (Base):
    __tablename__ = "chamados"

    id = Column (Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column (String(255), nullable=False)
    prioridade = Column (String(10), nullable=False)
    status = Column(String (10), nullable=False)
    data_criacao = Column(DateTime, nullable=False)
    data_fechamento = Column(DateTime)

    id_usuario = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False,
        )
    
    id_tecnico = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=True,
        )
    
    id_categoria = Column(
        Integer,
        ForeignKey("categorias.id"),
        nullable=False,
        )

    usuario = relationship (
        "User",
        foreign_keys=[id_usuario],
        back_populates="chamados_abertos"
    )

    tecnico = relationship(
        "User",
        foreign_keys=[id_tecnico],
        back_populates= "chamados_atendidos"
    )

    categoria = relationship(
        "Categoria",
        back_populates="chamados"
    )


