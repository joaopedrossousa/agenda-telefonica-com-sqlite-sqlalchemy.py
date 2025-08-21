from db.base import Base, engine
import models.contatos

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":

    from seed import criar_contato

    criar_contato()
