class Funcionario():
    def __init__(self, nome):
        self.nome = nome
    
    def descricao():
        pass

class Desenvolvedor(Funcionario):
    def __init__(self, nome, senioridade):
        super().__init__(nome)
        self.senioridade = senioridade

    def descricao(self):
        return f"meu nome é {self.nome} e eu sou {self.senioridade}"
    
class TechLead(Funcionario):
    def __init__(self, nome, anos_de_empresa):
        super().__init__(nome)
        self.anos_de_empresa = anos_de_empresa

    def descricao(self):
        return f"meu nome é {self.nome} e eu estou a {self.anos_de_empresa}"
    
if __name__ == "__main__":
    funcionarios = []
    d = Desenvolvedor("teco", "dev jr")
    tl = TechLead("Jr", 10)
    funcionarios.append(tl)
    funcionarios.append(d)

    for funcionario in funcionarios:
        print(funcionario.descricao())
    