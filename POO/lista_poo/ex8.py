class SensorDeKi():
    def __init__(self, nivel_ki):
        self.__nivel_ki = nivel_ki

    def get_ki(self):
        return self.__nivel_ki
    
    def set_ki(self, valor):
        if self.__nivel_ki >= 0 and self.__nivel_ki <= 9000:
            self.__nivel_ki = valor
            if self.__nivel_ki > 8000:
                return "é mais de 8000!"

if __name__ == "__main__":
    personagem = SensorDeKi(8000)
    print(personagem.set_ki(8001))
