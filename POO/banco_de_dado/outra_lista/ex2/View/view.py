from Model.Base import Base, Banco
from Model.Produto import Produto
from sqlalchemy.orm import Session 

bd = Banco('sqlite:///usuarios.db')
Base.metadata.create_all(bd.get_engine())

with Session(bd.get_engine()) as session:
    while True:
        print('1-adiciona produto\n2-atualiza preco\n3-atualiza estoque\n4-lista produtos\n0-sair')
        op = int(input('Escolha um: '))

        match op:
            case 1:
                nome = input('nome: ')
                preco = input('preco: ')
                estoque = input('estoque: ')
                produto = Produto(nome, preco, estoque)
                session.add(produto)
                session.commit()
            
            case 2:
                id = int(input('ID do produto a atualizar: '))
                produto = session.query(Produto).filter_by(id=id).first()
                if produto:
                    preco = input('novo preco: ')
                    produto.set_preco(preco)
                    session.commit()
            case 3:
                id = int(input('ID do produto a atualizar: '))
                produto = session.query(Produto).filter_by(id=id).first()
                if produto:
                    estoque = input('novo estoque: ')
                    produto.set_estoque(estoque)
                    session.commit()
            case 4:
                produtos = session.query(Produto).all()
                for c in produtos:
                    print(f'{c.id} | {c.nome} | {c.preco} | {c.estoque}')
            case 0:
                break