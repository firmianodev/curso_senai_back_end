class Arena():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.largura * self.altura
        return area
    
    def calcular_perimetro(self):
        perimetro = (2 * self.altura) + (2 * self.largura)
        return perimetro

if __name__ == "__main__":
    pass