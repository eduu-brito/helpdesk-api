from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Comentario(Base):
    __tablename__ = "comentarios"

    id = Column(Integer, primary_key=True)
    conteudo = Column(String(500), nullable=False)
    data_criacao = Column(DateTime, nullable=False)

    id_usuario = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )

    id_chamado = Column(
        Integer,
        ForeignKey("chamados.id"),
        nullable=False
    )

    usuario = relationship(
        "User",
        back_populates="comentarios"
    )

    chamado = relationship(
        "Chamado",
        back_populates="comentarios"
    )