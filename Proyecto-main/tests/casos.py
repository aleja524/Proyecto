import unittest
import logica



class CalcularAhorroProgramado(unittest.TestCase):

      # Casos normales 

    def test_intereses_mensual(self):
        monto_inicial = 10_000_000
        aporte_periodico = 500_000
        n_periodos = 12
        tasa_interes = 0.01

        resultado = logica.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 17_609_502

        self.assertAlmostEqual(esperado, resultado, delta=1)

    def test_mayor_tasa_interes(self):
        monto_inicial = 20_000_000
        aporte_periodico = 1_000_000
        n_periodos = 24
        tasa_interes = 0.015

        resultado = logica.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 57_223_577

        self.assertAlmostEqual(esperado, resultado, delta=1)

    def test_estandar(self):
        monto_inicial = 5_000_000
        aporte_periodico = 250_000
        n_periodos = 12
        tasa_interes = 0.01

        resultado = logica.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 8_804_751  

        self.assertAlmostEqual(esperado, resultado, delta=1)



          # Casos extraordinarios


    def test_0_intereses(self):
        monto_inicial = 1_000_000
        aporte_periodico = 50_000
        n_periodos = 12
        tasa_interes = 0

        resultado = logica.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 1_600_000

        self.assertAlmostEqual(esperado, resultado, delta=1)

    def test_periodos_cortos(self):
        monto_inicial = 1_700_000
        aporte_periodico = 80_000
        n_periodos = 4
        tasa_interes = 0.01

        resultado = logica.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 2_093_859

        self.assertAlmostEqual(esperado, resultado, delta=1)

    def test_sin_monto_inicial(self):
        monto_inicial = 0
        aporte_periodico = 1_000_000
        n_periodos = 12
        tasa_interes = 0.01

        resultado = logica.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        esperado = 12_682_503  

        self.assertAlmostEqual(esperado, resultado, delta=1)


       #Casos de error

    def test_error_monto_inicial_negativo(self):
        monto_inicial = -15_000_000
        aporte_periodico = 400_000
        n_periodos = 36
        tasa_interes = 0.01
        with self.assertRaises(logica.monto_inicial):
            logica.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)


     

    def test_error_aporte_periodico_0(self):
        monto_inicial = 150_000
        aporte_periodico = 0
        n_periodos = 25
        tasa_interes = 0.01
        with self.assertRaises(logica.aporte_periodico):
            logica.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)





  

    def test_error_superior_periodps_mayor_60(self):
        monto_inicial = 200_000
        aporte_periodico = 16_000_000
        n_periodos = 200
        tasa_interes = 0.01
        with self.assertRaises(logica.aporte_periodico):
            logica.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)
  






    def test_error_tasa_interes_negativa(self):
        monto_inicial = 205_000
        aporte_periodico = 500_000
        n_periodos = 15
        tasa_interes = -1
        with self.assertRaises(logica.tasa_interes_negativa):
            logica.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)
  

    




if __name__ == '__main__':
    unittest.main()
