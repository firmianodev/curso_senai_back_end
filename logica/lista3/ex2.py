def media(nota1, nota2, nota3, procedimento):
    if procedimento == "A":
        media = (nota1 + nota2 + nota3) / 3
    elif procedimento == "P":
        media = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / 10
    else:
        media = 3 / (1 / nota1) + (1 / nota2) + (1/nota3)
    return media

def main():
    medianota = media(10, 8, 9, "H")   
    print(medianota)

if __name__ == "__main__":
    main()