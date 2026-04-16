class ContaJogador():
    def __init__(self, nickname, xp):
        self.nickname = nickname
        self.xp = xp

    def exibir_status(self):
        print(f"nome: {self.nickname} | xp: {self.xp}")
    
    def ganhar_xp(self, valor):
        self.xp += valor
        self.exibir_status()

    def gasta_xp(self, valor):
        self.xp -= valor
        self.exibir_status()

if __name__ == "__main__":
    personagem = ContaJogador("teco", 10000)
    personagem.ganhar_xp(500)
    personagem.gasta_xp(200)