vetor = []
soma = 0

for i in range(3):
    numero = int(input("digite um numero: "))
    vetor.append(numero)

for valor in vetor:
    soma += valor
    media = soma / 3

print(f"{media:.2f}")