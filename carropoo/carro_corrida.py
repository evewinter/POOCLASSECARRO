from carro import Carro

class CarroCorrida(Carro):
    def __init__(self, velocidade_inicial):
        super().__init__(velocidade_inicial)
        
    def acelera(self):
        self.velocidade += 500
        print("aceleração de carrida a velocidade aumentou em 500km\h")