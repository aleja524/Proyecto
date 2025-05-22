import sys
import os
# asegurarnos de añadir la carpeta src desde la ubicación de este archivo
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import unittest
from model import logic



class CalcularAhorroProgramado(unittest.TestCase):

    # Casos normales 
    
    
#En este caso, es un caso normal con intereses   
    def test_intereses_mensual(self):
        monto_inicial = 10_000_000
        aporte_periodico = 500_000
        numero_periodos = 12
        tasa_interes = 0.01
        resultado = logic.calcular_monto(monto_inicial, tasa_interes, numero_periodos, aporte_periodico)
        esperado = 17_609_502
        self.assertAlmostEqual(esperado, resultado, delta=1)


#En este caso es caso normal con una tasa de interes alta
    def test_mayor_tasa_interes(self):
        monto_inicial = 20_000_000
        aporte_periodico = 1_000_000
        numero_periodos = 24
        tasa_interes = 0.015

        resultado = logic.calcular_monto(monto_inicial, tasa_interes, numero_periodos, aporte_periodico)

        esperado = 57_223_577

        self.assertAlmostEqual(esperado, resultado, delta=1)


#Este es un caso normal como se suele hacer un ahorro común 
    def test_estandar(self):
        monto_inicial = 5_000_000
        aporte_periodico = 250_000
        numero_periodos = 12
        tasa_interes = 0.01

        resultado = logic.calcular_monto(monto_inicial, tasa_interes, numero_periodos, aporte_periodico)

        esperado = 8_804_751  

        self.assertAlmostEqual(esperado, resultado, delta=1)




          # Casos extraordinarios

#Este es un caso extraordinario con la tasa de interes en 0
    def test_0_intereses(self):
        monto_inicial = 1_000_000
        aporte_periodico = 50_000
        numero_periodos = 12
        tasa_interes = 0

        resultado = logic.calcular_monto(monto_inicial, tasa_interes, numero_periodos, aporte_periodico)

        esperado = 1_600_000

        self.assertAlmostEqual(esperado, resultado, delta=1)


#Este es un caso extraordinario con número de periodos cortos
    def test_periodos_cortos(self):
        monto_inicial = 1_700_000
        aporte_periodico = 80_000
        numero_periodos = 4
        tasa_interes = 0.01

        resultado = logic.calcular_monto(monto_inicial, tasa_interes, numero_periodos, aporte_periodico)

        esperado = 2_093_859

        self.assertAlmostEqual(esperado, resultado, delta=1)



#Caso extraordinario con monto inicial en 0
    def test_sin_monto_inicial(self):
        monto_inicial = 0
        aporte_periodico = 1_000_000
        numero_periodos = 12
        tasa_interes = 0.01

        resultado = logic.calcular_monto(monto_inicial, tasa_interes, numero_periodos, aporte_periodico)

        esperado = 12_682_503  

        self.assertAlmostEqual(esperado, resultado, delta=1)




       #Casos de error

#Este es un caso de error donde no se puede poner un monto inicial negativo
    def test_error_monto_inicial_negativo(self):
        monto_inicial = -15_000_000
        aporte_periodico = 400_000
        numero_periodos = 36
        tasa_interes = 0.01
        with self.assertRaises(logic.monto_inicial_negativo):
            logic.calcular_monto(monto_inicial, tasa_interes, numero_periodos, aporte_periodico)


     
#Caso de error donde el aporte periodico no puede ser menor o igual a 0
    def test_error_aporte_periodico_0(self):
        monto_inicial = 150_000
        aporte_periodico = 0
        numero_periodos = 25
        tasa_interes = 0.01
        with self.assertRaises(logic.aporte_periodico_menor_a_cero):
            logic.calcular_monto(monto_inicial, tasa_interes, numero_periodos, aporte_periodico)





  
#Caso de error donde el número de periodos no puede ser mayor a 60
    def test_error_superior_periodps_mayor_60(self):
        monto_inicial = 200_000
        aporte_periodico = 16_000_000
        numero_periodos = 200
        tasa_interes = 0.01
        with self.assertRaises(logic.aporte_periodico_mayor_a_60):
            logic.calcular_monto(monto_inicial, tasa_interes, numero_periodos, aporte_periodico)
  





#Caso de error donde la tasa no puede iniciar negativa
    def test_error_tasa_interes_negativa(self):
        monto_inicial = 205_000
        aporte_periodico = 500_000
        numero_periodos = 15
        tasa_interes = -1
        with self.assertRaises(logic.tasa_interes_negativa):
            logic.calcular_monto(monto_inicial, tasa_interes, numero_periodos, aporte_periodico)
  

    




if __name__ == '__main__':
    unittest.main()
