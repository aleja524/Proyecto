import unittest
import casos_pruebas.calculos

class calculara_programada(unittest.TestCase):
    def test_intereses_mensual(self):
        monto_inicial = 10_000_000
        aporte_periodico = 500_000
        n_periodos = 12
        tasa_interes = 0.01

        resultado = casos_pruebas.calculos.calcular_monto(monto_inicial,aporte_periodico,n_periodos,tasa_interes)

        esperado = 17_609_502

        self.assertAlmostEqual(esperado,resultado,0)


    def test_mayor_tasa_interes(self):
        monto_inicial = 20_000_000
        aporte_periodico = 1_000_000
        n_periodos = 24
        tasa_interes = 0.015

        resultado = casos_pruebas.calculos.calcular_monto(monto_inicial,aporte_periodico,n_periodos,tasa_interes)

        esperado = 57_223_577

        self.assertAlmostEqual(esperado,resultado,0)  


    def test_estanmdar(self):
        monto_inicial = 5_000_000
        aporte_periodico = 250_000
        n_periodos = 12
        tasa_interes = 0.01

        resultado = casos_pruebas.calculos.calcular_monto(monto_inicial,aporte_periodico,n_periodos,tasa_interes)

        esperado = 17_609_502

        self.assertAlmostEqual(esperado,resultado,0)       

if __name__ == '__main__':
    unittest.main()