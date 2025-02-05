from carro_inteligente import Carrointeligente
from carro_esportivo import Carroesportivo
from carro_corrida import CarroCorrida

def test_drive(carro):
    print(f"\ntestando {carro.__class__.__name__}:")
    carro.exibe_velocidade()
    carro.acelera()

if __name__ == "__main__":
    carro_inteligente = Carrointeligente(10)
    print("Carro inteligente:")
    carro_inteligente.estacionar()
    test_drive(carro_inteligente)
    print()
    
    carro_esportivo = Carroesportivo(50)
    print("carro esportivo:")
    carro_esportivo.turbo()
    test_drive(carro_esportivo)
    
    carro_corrida = CarroCorrida(100)
    test_drive(carro_corrida)