from Models.Heroi import Heroi

s = Heroi.session()

def inicializar():
    Heroi.criar_tabela()


def inserir_heroi(nome: str, classe: str) -> Heroi:
    try:
        heroi = Heroi(nome=nome, classe=classe, nivel = 1, pontosExperiencia = 0 ) 
        s.add(heroi)     
        s.commit()       
        s.refresh(heroi) 
        return heroi
    except Exception as e:
        s.rollback()
        raise e 
    
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
    
    

