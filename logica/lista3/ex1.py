def Calcular_Area(raio):
    area = 3.14 * (raio**2)
    return area

def main():
    raio = float(input("Digite o raio do circulo"))

    area = Calcular_Area(raio)
    print(area)

if __name__ == "__main__":
    main()

