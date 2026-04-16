vetor = []
count = 0

for i in range(3):
    numero = int(input("digite um numero: "))
    vetor.append(numero)
    if numero > 8:
        count += 1

print(f"ha {count} numeros maiores que 8")