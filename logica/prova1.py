import random

def gera_numero():
    return random.randint(0, 100)

def verifica_numero_escolhido(valor_tentativa, numero_gerado):
    if valor_tentativa < numero_gerado:
        return (f"O numero escondido é maior que o numero que vc esoclheu")
    return (f"O numero escondido é menor que o numero que vc escolheu, restam ")

def gera_dificuldade(dificuldade):
    if dificuldade == "facil":
        return 10
    elif dificuldade == "medio":
        return 5
    else: 
        return 1
    
def gera_pontuacao(pontuacao):
    pontuacao += 10
    return pontuacao

def jogo():
    pontuacao = 0
    numero_gerado = gera_numero()
    while True:
        dificuldade = input("Qual dificuldade vc quer jogar? (facil, medio, dificil) ").lower()
        max_tentativas = gera_dificuldade(dificuldade)
        tentativas = max_tentativas

        while max_tentativas >= 0:
            print(numero_gerado)
            valor_tentativa = float(input("Digite o valor de um numero para tentar adivinhar o numero escondido: "))
            tentativas -= 1

            if valor_tentativa == numero_gerado:
                pontuacao = gera_pontuacao(pontuacao)
                print(f"Voce venceu! O numero {numero_gerado} era o certo!, voce tem {pontuacao} pontos")
                numero_gerado = gera_numero()
            else:
                print(verifica_numero_escolhido(valor_tentativa, numero_gerado), f",restam {tentativas} tentativas.")
                if tentativas == 0:
                    print("Voce perdeu")
                    break


        parada = input("Parar de jogar? (y/n)")
        if parada == "y":
            print("fim de jogo")
            break    

def main():
    jogo()

if __name__ == "__main__":
    main()