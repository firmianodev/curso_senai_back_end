class Personagm:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

    def __str__(self):
        return f'Nome: {self.nome} | poder: {self.poder}'

if __name__ == "__main__":
    personagem = Personagm("flash", "velocidade")

    print(personagem)