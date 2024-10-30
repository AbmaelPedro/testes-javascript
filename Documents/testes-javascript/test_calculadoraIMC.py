from calculadoraIMC import Calculadora_imc  # Importação da classe
import unittest  # Importação do pacote de testes unitários

class TestCalculadoraIMC(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora_imc()  # Objeto da classe Calculadora

    def test_calculo_imc(self):
        self.assertEqual(self.calc.calculo_imc(75, 1.74), 'Acima do peso', "Deve retornar Acima do peso")

if __name__ == "__main__":
    unittest.main()
