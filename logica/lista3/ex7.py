def verifica_numero_perfeito(numero):
    soma = 0
    for i in range(numero-1):
        if numero % (i + 1) == 0:
            soma += i + 1

    return "é um numero perfeito"
    
def main():
    print(verifica_numero_perfeito(6))

if __name__ == "__main__":
    main()
