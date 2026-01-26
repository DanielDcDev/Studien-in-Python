class Motor:
    def ligar(self):
        print("Motor ligado")

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar(self):
        self.motor.ligar()

class Barco:
    def __init__(self):
        self.motor = Motor()

    def ligar(self):
        self.motor.ligar()
