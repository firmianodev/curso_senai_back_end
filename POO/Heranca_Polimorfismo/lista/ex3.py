class Forma():
    def __init__(self):
        pass

    def area():
        pass

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14

    def area(self):
        return self.pi * self.raio
    
class Retangulo(Forma):
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura
    
if __name__ == "__main__":
    c = Circulo(5)
    print(c.area())
    r = Retangulo(10, 25)
    print(r.area())