class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * .05
    
class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario * 0.1
    
class Vendedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):
        return self.salario * 0.08

if __name__ =="__main__":
    g = Gerente("teco", 10000)
    print(g.calcular_bonus()) 

    v = Vendedor("vendedor", 5000)
    print(v.calcular_bonus())