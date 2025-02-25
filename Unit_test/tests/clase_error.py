import calculos
class ahorro_negativo ():
    """No se puede poner valores negativos"""
    
    def test_error_intereses_mensual(self):
        monto_inicial = -15_000_000
        aporte_periodico = 400_000
        n_periodos = 36
        tasa_interes = 0.01
        esperado = -4_230_780
        resultado = calculos.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)

        self.assertAlmostEqual(esperado, resultado, delta=1)




class aporte_periodico_mayor_60():
    """No se puede poner aportes periodicos mayores a 200 años"""     

    def test_error_aporte_periodico_0(self):
        monto_inicial = 150_000
        aporte_periodico = 0
        n_periodos = 25
        tasa_interes = 0
        resultado = calculos.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)
        esperado = 150_000
        self.assertAlmostEqual(esperado, resultado, delta=1)   






class tasa_interes_negativa():
    """No se puede poner tasa de interes negativa"""     

    def test_error_aporte_periodico_0(self):
        monto_inicial = 150_000
        aporte_periodico = 0
        n_periodos = 25
        tasa_interes = 0
        resultado = calculos.calcular_monto(monto_inicial, tasa_interes, n_periodos, aporte_periodico)
        esperado = 150_000
        self.assertAlmostEqual(esperado, resultado, delta=1)   



