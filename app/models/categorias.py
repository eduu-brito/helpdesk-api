from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True)
    nome = Column(String(150),nullable=False)

    chamados = relationship(
       "Chamado",
       back_populates= "categoria"
    )
