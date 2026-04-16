def verifica_positivo(valor):
    if valor % 1 == valor and valor % valor == 1:
        return True
    else:
        return False

def main():
    teste = verifica_positivo(7)
    print(teste)

if __name__ == "__main__":
    main()