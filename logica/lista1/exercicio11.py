if __name__ == "__main__":

    preco_produto = float(input("Digite o preco do produto: "))
    condicao_pagamento = int(input("Digite a condicao de pagamento (1-4)"))

    match condicao_pagamento:
        case 1:
            preco_produto *= 0.9
        case 2:
            preco_produto *= 0.85
        case 3:
            preco_produto = preco_produto
        case 4:
            preco_produto *= 1.1
        case _:
            print("Condicao de pagamento invalida")
    print(f"O preco final do produto é: R$ {preco_produto:.2f}")
