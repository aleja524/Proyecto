import unittest
import calculos

class CalcularAhorroProgramado(unittest.TestCase):
    def test_intereses_mensual(self):
        monto_inicial = 1_000_000
        aporte_periodico = 50_000
        n_periodos = 12
        tasa_interes = 0

        resultado = calculos.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 1_600_000

        self.assertAlmostEqual(esperado, resultado, delta=1)

    def test_mayor_tasa_interes(self):
        monto_inicial = 1_700_000
        aporte_periodico = 80_000
        n_periodos = 4
        tasa_interes = 0.01

        resultado = calculos.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 2_093_859

        self.assertAlmostEqual(esperado, resultado, delta=1)

    def test_estandar(self):
        monto_inicial = 0
        aporte_periodico = 1_000_000
        n_periodos = 12
        tasa_interes = 0.01

        resultado = calculos.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 12_682_503  

        self.assertAlmostEqual(esperado, resultado, delta=1)

if __name__ == '__main__':
    unittest.main()
