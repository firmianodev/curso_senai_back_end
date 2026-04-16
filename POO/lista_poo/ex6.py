class ContaJogador():
    def __init__(self, nickname):
        self.nickname = nickname
        self.__xp = None

    @property
    def get_xp(self):
        return self.xp

    def exibir_status(self):
        print(f"nome: {self.nickname} | xp: {self.xp}")
    
    def ganhar_xp(self, valor):
        self.xp += valor
        self.exibir_status()

    def gasta_xp(self, valor):
        self.xp -= valor
        self.exibir_status()
