class Animal():
    def __init__(self, nome):
        self.nome = nome

    def fazer_som():
        return "som"
    
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(sef):
        return "auau"
    
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        return "miau"
    
class Passaro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        return "piu"
    
def faz_som(animal):
    return animal.fazer_som()
    
if __name__ == "__main__":
    c = Cachorro("rex")
    print(c.fazer_som())

    g = Gato("preto")
    print(g.fazer_som())

    p = Passaro("blue")
    print(p.fazer_som())

    print(faz_som(c))