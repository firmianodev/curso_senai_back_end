valores = [0,0,0]
valores[0] = float(input("digiite um valor"))
valores[1] = float(input("digiite um valor"))
valores[2] = float(input("digiite um valor"))

if valores[0] != valores[1] and valores[1] != valores[2]:
    valores.sort(reverse=True)

    print(valores)