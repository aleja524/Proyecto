import unittest
import calculos

class CalcularAhorroProgramado(unittest.TestCase):
    def test_intereses_mensual(self):
        monto_inicial = 10_000_000
        aporte_periodico = 500_000
        n_periodos = 12
        tasa_interes = 0.01

        resultado = calculos.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 17_609_502

        self.assertAlmostEqual(esperado, resultado, delta=1)

    def test_mayor_tasa_interes(self):
        monto_inicial = 20_000_000
        aporte_periodico = 1_000_000
        n_periodos = 24
        tasa_interes = 0.015

        resultado = calculos.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 57_223_577

        self.assertAlmostEqual(esperado, resultado, delta=1)

    def test_estandar(self):
        monto_inicial = 5_000_000
        aporte_periodico = 250_000
        n_periodos = 12
        tasa_interes = 0.01

        resultado = calculos.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 8_804_751  

        self.assertAlmostEqual(esperado, resultado, delta=1)

if __name__ == '__main__':
    unittest.main()
