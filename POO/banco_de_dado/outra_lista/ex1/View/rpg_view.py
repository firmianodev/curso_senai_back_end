from Model.Mago import Mago
from Controller.luta import lutar

def view():
    nome = input("nome: ")
    p1 = Mago(nome)

    nome = input("nome: ")
    p2 = Mago(nome)

    lutar(p1, p2)