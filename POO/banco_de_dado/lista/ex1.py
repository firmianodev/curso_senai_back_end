from sqlalchemy import create_engine 
from sqlalchemy import DeclarativeBase, Mapped, mapped_column, Session 

class Banco:
    def __init__(self, url):
        self.__engine = create_engine(url)

    def get_engine(self):
        return self.__engine
    
class Base(DeclarativeBase):
    pass

class Usuario(Base):
    __tablename__ = 'usuarios'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()


if __name__ == "__main__":
    bd = Banco('sqlite:///usuarios.db')
    Base.metadata.create_all(bd.get_engine())

    with Session(bd.get_engine()) as session:
        while True:
            print('1 - adicionar usuarios\n 2- listar usuarios\n0- sair')

            op = int(input('escolha uma opcao: '))

            match op:
                case 1:
                    nome = input('Digite o nome do contato: ')
                    email = input('Digite um email')
                    usuario = Usuario(nome = nome, email = email)
                    session.add(usuario)
                    session.commit()
                case 2:
                    usuarios = session.query(Usuario).all()
                    for c in usuarios:
                        print(f'{c.id} | {c.nome} | {c.email} | {c.telefone}')
                case 0:
                    break

