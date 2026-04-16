vetor = []
soma = 0

for i in range(10):
    numero = int(input("digite um numero: "))
    vetor.append(numero)

for valor in vetor:
    soma += valor

print(soma)