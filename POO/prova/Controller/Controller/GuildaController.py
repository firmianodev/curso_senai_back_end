from Models.Heroi import Heroi
from Models.Banco import session
s = session()


def inserir_heroi(nome: str, classe: str) -> Heroi:
    heroi = Heroi(nome, classe) 
    s.add(heroi)     
    s.commit()       
    s.refresh(heroi) 
    return heroi
    
def listar_herois():
    herois = s.query(Heroi).all()
    return herois

def buscar_heroi(id):
    heroi = s.get(Heroi, id)
    return heroi

def remover_heroi(id):
    heroi = s.get(Heroi, id)
    if heroi:
        s.delete(heroi)
        s.commit()