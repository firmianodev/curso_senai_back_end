if __name__ == "__main__":

    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))

    imc = peso / (altura ** 2)

    if imc < 18.5:
        print("Abaixo do peso")
    if 18.5 >= imc and imc < 25:
        print("A pessoa esta com o pesso normal")
    if imc >= 25:
        print("Pessoa esta com sobre peso")
    if imc >= 30:
        print("A pessoa está obesa")