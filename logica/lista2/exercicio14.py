vetor = []
count101_200 = 0
count_maior_200 = 0

for i in range(3):
    numero = int(input("digite um numero: "))
    vetor.append(numero)
    if numero > 100 and numero < 200:
        count101_200 += 1
    if numero > 200:
        count_maior_200 += 1

print(f"Ha {count101_200} numeros entre 101 e 200 \nHa {count_maior_200} numeros maiores que 200")