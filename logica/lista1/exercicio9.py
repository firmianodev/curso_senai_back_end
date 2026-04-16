altura = float(input("Digite sua altura: "))
sexo = input("Digite seu sexo: ")

if sexo == "M":
    peso_ideal = (72.7 * altura) - 58
if sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7

print(f"o peso ideal é {peso_ideal:.2f} kg")

