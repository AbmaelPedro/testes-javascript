
class Calculadora_imc:
    
    def calculo_imc(self, peso, altura):
        imc = peso / (altura **2)
        
        if peso <= 0 or altura <= 0:
            print('Os valores precisam ser números válido')

        if imc < 19:
            resultado = 'Magreza'

        elif imc >= 19 and imc < 24:
            resultado = 'Normal'

        elif imc >= 24 and imc < 29:
            resultado = 'Acima do peso'

        else:
            resultado = 'Obesidade' 
        
        return resultado
    