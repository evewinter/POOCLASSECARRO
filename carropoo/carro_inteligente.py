from carro import Carro

class Carrointeligente(Carro):
    def __init__(self,velocidade_inicial):
        super().__init__(velocidade_inicial)
    
    def estacionar(self):
        print("estacionando automaticamente...")