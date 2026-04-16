def mostra_categoria_nadador(idade):
    if idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 10:
        return "Infantil B"
    elif idade >= 11 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil b"
    else:
        return "Adulto"
    
def main():
    print(mostra_categoria_nadador(10))

if __name__ == "__main__":
    main()