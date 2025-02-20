def calcular_monto(P, r, n, d):
    """
    Calcula el monto final de un ahorro con interés compuesto.

    :param P: Monto inicial
    :param r: Tasa de interés por período (Ejemplo: 0.01 para 1%)
    :param n: Número de períodos (Ejemplo: 12 meses)
    :param d: Aporte periódico (mensual, anual, etc.)
    :return: Monto final A
    """
    if r == 0:  # Caso sin interés
        return P + (d * n)

    return P * (1 + r) ** n + d * (((1 + r) ** n - 1) / r)


#  Casos de prueba con valores esperados
casos_de_prueba = [
    (10_000_000, 0.01, 12, 500_000, 18_609_502),  # Caso 1
    (20_000_000, 0.015, 24, 1_000_000, 57_223_577),  # Caso 2
    (5_000_000, 0.01, 12, 250_000, 8_804_751),  # Caso 3
]

# 🔹 Ejecutamos las pruebas
for i, (P, r, n, d, esperado) in enumerate(casos_de_prueba, start=1):
    resultado = round(calcular_monto(P, r, n, d))  # Redondeamos para comparar mejor
    if resultado == esperado:
        print(f"Ok {i}: Correcto  {resultado} es igual a {esperado}")
    else:
        print(f" Valor diferente {i}: Incorrecto  Se obtuvo {resultado}, pero se esperaba {esperado}")

