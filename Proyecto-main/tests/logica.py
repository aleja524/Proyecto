
class monto_inicial( Exception ):
   """El monto inicial no puede ser inferior a 0"""
   pass


# Error cuando ingresan una compra menor o igual a cero
class aporte_periodico( Exception ):
   """El monto de los periodos debe ser mayor de 0 y menor de 60"""
   pass


class tasa_interes_negativa(Exception):
    """No puede ser negativa la tasa de intereses """
    pass


# casos_pruebas/calculos.py
def calcular_monto(P, r, n, d):
   
    if r == 0:  # Caso sin interés
        return P + (d * n)

    if P < 0:
        raise monto_inicial("ERROR: El monto inical no puede ser negativo")
    
    if d == 0:
        raise aporte_periodico("ERROR: El aporte peridico debe ser mayor a 0")
    
    if d < 0:
        raise aporte_periodico("ERROR: El aporte periodico tiene que ser mayor a 0")
    
    if n >60:
        raise aporte_periodico("ERROR: el numero de periodos debe ser menor que 60")
    
    if r < 0:
        raise tasa_interes_negativa("ERROR: La tasa de interes no puede ser negativa")
    
    return P * (1 + r) ** n + d * (((1 + r) ** n - 1) / r)

    

    











    

