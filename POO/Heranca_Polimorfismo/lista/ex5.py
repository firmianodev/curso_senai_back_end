class ContaBancaria():
    def __init__(self, nome, cpf, saldo):
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo
    
    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    
class ContaCorrente(ContaBancaria):
    def __init__(self, nome, cpf, saldo):
        super().__init__(nome, cpf, saldo)
    
    def sacar(self, valor):
        return super().sacar(valor) * 1.001
    
class ContaPoupanca(ContaBancaria):
    def __init__(self, nome, cpf, saldo):
        super().__init__(nome, cpf, saldo)

    def sacar(self, valor):
        return super().sacar(valor) * 1.008
        
if __name__ == "__main__":
    cc = ContaCorrente("teco", 1234, 10000)
    print(cc.sacar(1000))

    cp = ContaPoupanca("jr", 654321, 10000)
    print(cp.sacar(1000))