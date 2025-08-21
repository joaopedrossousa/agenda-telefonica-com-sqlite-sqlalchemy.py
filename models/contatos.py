from db.base import Base
from sqlalchemy import Column, String, Integer


class Contato(Base):
    __tablename__ = "contatos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, nullable=True)
    numero_telefone = Column(String, nullable=True)

    def __init__(self, nome, numero_telefone):

        self.nome = nome
        self.numero_telefone = numero_telefone
