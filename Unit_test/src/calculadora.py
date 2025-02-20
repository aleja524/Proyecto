def calcular_monto(P, r, n, d):
    """
    Calcula el monto final de un ahorro con interés compuesto.

    :param P: Monto inicial
    :param r: Tasa de interés por período
    :param n: Número de períodos
    :param d: Aporte periódico
    :return: Monto final A
    """
    if r == 0:  # Caso sin interés
        return P + (d * n)
    
    return P * (1 + r) ** n + d * (((1 + r) ** n - 1) / r)
