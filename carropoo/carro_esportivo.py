from carro import Carro

class Carroesportivo(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)
    def turbo(self):
        self.velocidade +=10
        print('turbo ativado a velocidade aumentou em 10 km/h')