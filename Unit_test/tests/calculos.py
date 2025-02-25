# casos_pruebas/calculos.py
def calcular_monto(P, r, n, d):
    if P < 0:
        raise Exception ("el monto inicial no puede ser negativo")
    if r == 0:  # Caso sin interés
        return P + (d * n)
    return P * (1 + r) ** n + d * (((1 + r) ** n - 1) / r)

    

