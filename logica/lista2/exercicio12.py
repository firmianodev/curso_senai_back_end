vetor = []
count = 0
count = 0

for i in range(3):
    numero = int(input("digite um numero: "))
    vetor.append(numero)
    if numero % 2 == 0:
        count += 1
    else:
        count_impar += 1

print(f"Ha {count} numeros pares\nHa {count_impar} numeros impares")