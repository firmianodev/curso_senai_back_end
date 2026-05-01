from Models.Missao import Missao
from Models.Heroi import Heroi
from Models.Banco import session

s = session()

def cadrasta_missao(titulo: str, descricao: str, recompensa_xp: int, heroi_id: int) -> Missao:

    missao = Missao(titulo=titulo, descricao=descricao, recompensa_xp=recompensa_xp, heroi_id=heroi_id, status = "pendente" ) 
    s.add(missao)     
    s.commit()       
    s.refresh(missao) 
    return missao

def concluir_missao(missao_id):
    try:
        missao = s.get(Missao, missao_id)

        if missao is None:
            raise ValueError(f"Missão com id {missao_id} não encontrada.")

        if missao.status == "concluida":
            raise ValueError(f"A missão '{missao.titulo}' já foi concluída anteriormente.")
        else:
            heroi = s.get(Heroi, missao.heroi_id)

            if heroi is None:
                raise ValueError(f"Herói associado à missão não encontrado.")

            missao.status = "concluida"
            heroi.pontosExperiencia += missao.recompensa_xp

            s.commit()
            s.refresh(missao)
            return missao
    except Exception as e:
        s.rollback()
        raise e