class Pokemon:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def __str__(self):
        return f'{self.nome} usou um ataque do tipo {self.tipo}!'

if __name__ == "__main__":
    personagem = Pokemon("charmander", "fogo")
    print(personagem)