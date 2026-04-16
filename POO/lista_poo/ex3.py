class NaveEspacial():
    def __init__(self, nome, velocidade):
        self.nome = nome
        self.velocidade = velocidade

    def exibir_status(self):
        print(f"nome: {self.nome} | velocidade: {self.velocidade}")

if __name__ == "__main__":
    nave = NaveEspacial("b2", "mach1")
    nave.exibir_status()