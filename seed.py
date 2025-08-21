from db.base import SessionLocal
from models.contatos import Contato


def criar_contato():
    nome = input("Informe o nome: ")
    numero = input("Informe o numero: ")

    with SessionLocal() as session:
        novo_contato = Contato(nome=nome, numero_telefone=numero)
        session.add(novo_contato)
        session.commit()
