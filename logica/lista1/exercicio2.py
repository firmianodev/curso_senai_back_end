if __name__ == "__main__":
    nome = input("Digite o nome: ")
    sexo = input("Digite o sexo: (f/m)")
    estado_civil = input("Digite o estado civil: ")

    if sexo.lower() == "f" and estado_civil.lower() == "Casada":
        anos_casada = input("Quantos anos está casada?")