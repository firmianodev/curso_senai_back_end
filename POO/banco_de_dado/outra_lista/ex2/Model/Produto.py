from Model import Base 
from sqlalchemy.orm import Mapped, mapped_column

class Produto(Base):
    __tablename__ = 'usuarios'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column()
    preco: Mapped[str] = mapped_column()
    estoque: Mapped[str] = mapped_column()

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.set_preco(preco)
        self.set_estoque(estoque)
        
    def set_preco(self, preco):
        if preco < 0:
            raise ValueError("Preço não pode ser negativo.")
        self.preco = preco

    def set_estoque(self, estoque):
        if estoque < 0:
            raise ValueError("Estoque não pode ser negativo.")
        self.estoque = estoque