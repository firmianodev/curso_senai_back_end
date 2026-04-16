from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, Session

class Banco:
    def __init__(self, url):
        self.__engine = create_engine(url)

    def get_engine(self):
        return self.__engine
    
class Base(declarative_base):
    pass

class Contatos(Base):
    __tablename__ = 'contatos'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column()
    email: Mapped[str]
    telefone: Mapped[int]

if __name__ == "__main__":
    bd = Banco('sqlite:///contatos.db')
    Base.metadata.create_all(bd.get_engine())

    with Session(db.get_engine()) as session:
        while True:
            print('1 - adicionar contato')
            print('2 - listar contatos')
            print('3 - atualizar contato')
            print('4 - deletar contato')
            print('5 - buscar contato por id')
            print('0 - sair')

            op = int(input('Escolha uma opcao: '))

            match op:
                case 1:
                    nome = input('Digite o nome do contato: ')
                    email = input('Digite um email')
                    telefone = input('Digite o telefone do contato: ')

                    contato = Contatos(nome = nome, email = email, telefone = telefone)
                    session.add(contato)
                    session.commit()
                case 2:
                    contato = session.query(Contatos).all()

                    print(contato)

                    print('Contatos')
                    print('Id | Nome | Email | Telefone')
                    for c in contato:
                        print(f'{c.id} | {c.nome} | {c.email} | {c.telefone}')
                    

                case 3:
                    id = int(input('informe o id: '))
                    contato = session.query(Contatos).filter_by(id=id).first()

                    if contato:
                        nome = input('Digite o nome do contato: ')
                        email = input('Digite um email')
                        telefone = input('Digite o telefone do contato: ')

                        contato.nome = nome
                        contato.email = email
                        contato.telefone = telefone

                        session.commit()
                        print('')
                    else:
                        print('')
                case 4:
                    id = int(input('informe o id: '))
                    contato = session.query(Contatos).filter_by(id=id).first()

                    if contato:
                        session.delete(contato)
                        session.commit()
                        print('Contato deletado com sucesso!')
                    else:
                        print('contato nao encontrado')

                case 5:
                    id = int(input('informe o id: '))
                    contato = session.query(Contatos).filter_by(id=id).first()

                    if contato:
                        print(f"id: {contato.id}")
                        print(f"id: {contato.nome}")
                        print(f"id: {contato.email}")
                        print(f"id: {contato.telefone}")
                case 0:
                    print('saindo...')
                    break
