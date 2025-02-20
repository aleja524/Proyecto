# casos_pruebas/calculos.py
def calcular_monto(P, r, n, d):
    if r == 0:  # Caso sin interés
        return P + (d * n)
    return P * (1 + r) ** n + d * (((1 + r) ** n - 1) / r)
