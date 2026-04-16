vetor = []
count = 0

for i in range(3):
    numero = int(input("digite um numero: "))
    vetor.append(numero)
    if numero > 18:
        count += 1

print(count)

