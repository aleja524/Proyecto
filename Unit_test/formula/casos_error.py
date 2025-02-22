import unittest
import calculos

class CalcularAhorroProgramado(unittest.TestCase):
    def test_intereses_mensual(self):
        monto_inicial = -15_000_000
        aporte_periodico = 400_000
        n_periodos = 36
        tasa_interes = 0.01

        resultado = calculos.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = -4_230_780

        self.assertAlmostEqual(esperado, resultado, delta=1)

    def test_mayor_tasa_interes(self):
        monto_inicial = 150_000
        aporte_periodico = 0
        n_periodos = 25
        tasa_interes = 0

        resultado = calculos.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 150_000

        self.assertAlmostEqual(esperado, resultado, delta=1)


if __name__ == '__main__':
    unittest.main()
