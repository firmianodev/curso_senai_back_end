class Veiculo():
    def __init__(self, ano):
        self.ano = ano

    def mover(self):
        return "movendo..."
    
class Carro(Veiculo):
    def __init__(self, ano):
        super().__init__(ano)

    def mover(self):
        return "movendo sobre 4 rodas..."
    
class Bicicleta(Veiculo):
    def __init__(self, ano):
        super().__init__(ano)

    def mover(self):
        return "movendo sobre 2 rodas..."
    
if __name__ == "__main__":
    c = Carro(1900)
    print(c.mover())
    b = Bicicleta(1800)
    print(b.mover())