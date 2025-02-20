import unittest
from src.calculadora import calcular_monto

class TestCalculadora(unittest.TestCase):

    def validar_caso(self, P, r, n, d, esperado):
        """ Ejecuta la función, compara el resultado con el esperado y muestra mensaje. """
        resultado = calcular_monto(P, r, n, d)
        if round(resultado) == esperado:
            print(f" Prueba exitosa: {resultado} es igual a {esperado}")
        else:
            print(f" Error: Se obtuvo {resultado}, pero se esperaba {esperado}")
        self.assertEqual(round(resultado), esperado)  # Compara valores redondeados

    def test_casos_normales(self):
        print("\n Casos Normales:")
        self.validar_caso(10_000_000, 0.01, 12, 500_000, 17_609_502)
        self.validar_caso(20_000_000, 0.015, 24, 1_000_000, 57_223_577)
        self.validar_caso(5_000_000, 0.01, 12, 250_000, 8_804_751)

    def test_casos_error(self):
        print("\n Casos de Error:")
        self.validar_caso(-15_000_000, 0.01, 36, 400_000, -4_230_780)
        self.validar_caso(150_000, 0, 25, 0, 150_000)

    def tes_casos_extraordinaros(self):  
        print("\n Casos Extraordinarios:")
        self.validar_caso(1_000_000, 0, 12, 50_000, 1_600_000)
        self.validar_caso(1_700_000, 0.01, 4, 80_000, 2_093_859)
        self.validar_caso(0, 0.01, 12, 1_000_000, 12_682_503)  

if __name__ == '__main__':
    unittest.main()
