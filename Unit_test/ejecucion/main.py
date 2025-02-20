# ejecucion/main.py
import sys
sys.path.append('Unit_test')
from casos_pruebas import calcular_monto
from casos_pruebas.casos import casos_de_prueba_normal, casos_de_prueba_extraordinario

# Función para ejecutar las pruebas
def ejecutar_pruebas(casos_de_prueba, tipo="Normal"):
    print(f"Casos {tipo}")
    for i, (P, r, n, d, esperado) in enumerate(casos_de_prueba, start=1):
        resultado = round(calcular_monto(P, r, n, d))  # Redondeamos para comparar mejor
        
        if resultado == esperado:
            print(f" {i}: Correcto  {resultado} es igual a {esperado}")
        else:
            print(f" Incorrecto {i}: Se obtuvo {resultado}, pero se esperaba {esperado}")

# Bloque principal de ejecución
if __name__ == "__main__":
    ejecutar_pruebas(casos_de_prueba_normal, "Normal")
    ejecutar_pruebas(casos_de_prueba_extraordinario, "Extraordinario")

