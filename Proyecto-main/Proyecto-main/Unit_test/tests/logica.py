# casos_pruebas/calculos.py
def calcular_monto(P, r, n, d):
   
    if r == 0:  # Caso sin interés
        return P + (d * n)
    return P * (1 + r) ** n + d * (((1 + r) ** n - 1) / r)

def error(P, r, n, d):
    if P<0:
        raise error("ERROR: el monto inical no puede ser negativo")
    
    if d <= 0:
        raise error ("ERROR: el aporte peridico debe ser mayor a 0")
    
    if n >60:
        raise error ("ERROR: el numero de periodos debe ser menor que 60")
    











    

