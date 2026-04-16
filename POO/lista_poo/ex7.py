class Inventario():
    def __init__(self, nome, preco=None, peso=None, quantidade=None, itens=None):
        self.nome = nome
        self.preco = preco
        self.peso = peso
        self.quantidade = quantidade
        self.itens = []

    def set_preco(self, valor):
        if self.preco > 0:
            self.preco = valor
    
    def adiciona_item(self, nome):
       self.itens.append(nome)
       self.exibir_detalhes()

    def remover_item(self, nome):
        self.itens.remove(nome)
        self.exibir_detalhes()

    def exibir_detalhes(self):
        print(f"nome: {self.nome} | preco: {self.preco} | peso: {self.peso} | quantidade: {self.quantidade} | itens: {self.itens}")

if __name__ == "__main__":
    inventario = Inventario("estante")
    inventario.adiciona_item("lapis")
    inventario.adiciona_item("borracha")
    inventario.remover_item("lapis")
