from Controller.GuildaController import inserir_heroi, listar_herois
from Controller.MissaoController import cadrasta_missao, concluir_missao

def view():
    while True:
        
        op = int(input("1-Registrar heroi\n2-Listar herois\n3-Criar Missao\n4-concluir Missao\n0-Sair\n"))
        
        match op:
            case 1:
                nome = input("nome: ")
                classe = input("classe: ")
                inserir_heroi(nome, classe)
            case 2:
                listar_herois()
            case 3:
                titulo = input("titulo: ")
                descricao = input("descricao: ")
                recompensa_xp = int(input("xp: "))
                heroi_id = int(input("heroi id: "))
                cadrasta_missao(titulo, descricao, recompensa_xp, heroi_id)
            case 4:
                missao_id = int(input("missao id:"))
                concluir_missao(missao_id)
            case 0:
                break