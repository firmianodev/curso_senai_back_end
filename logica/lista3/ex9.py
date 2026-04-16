def verifica_positivo(numero):
    if numero > 0:
        return True
    else:
        return False
    
def main():
    teste = verifica_positivo(-10)
    print(teste)

if __name__ == "__main__":
    main()