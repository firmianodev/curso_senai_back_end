numero = 0.0
soma = 0
while True:

    numero = float(input("Digite um valor: "))
    if numero > 0:
        soma += numero
    if numero < 0:
        break
print(f"A soma dos numeros digitados é: {soma}")
