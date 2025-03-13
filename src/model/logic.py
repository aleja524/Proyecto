# Clases para los casos de error, es donde se pone en los casos que debe sacar excepción

class aporte_periodico_menor_a_cero( Exception ):
   """El monto de los periodos debe ser mayor de cero"""
   pass

class aporte_periodico_mayor_a_60( Exception ):
   """El monto de los periodos debe ser menor de 60"""
   pass


class tasa_interes_negativa(Exception):
    """No puede ser negativa la tasa de intereses """
    pass

class monto_inicial_negativo ( Exception ):
    """El monto inicial no puede ser negativa"""


# casos_pruebas/calculos.py
def calcular_monto(monto_inicial, tasa_interes, numero_periodos, aporte_periodico): 
   
    if tasa_interes == 0:  # Caso sin interés
        return monto_inicial + (aporte_periodico * numero_periodos)

    if monto_inicial < 0: # Caso con monto inicial menor a cero
        raise monto_inicial_negativo("ERROR: El monto inicial no puede ser negativo")
    
    if aporte_periodico == 0: #Caso de aporte periodico mayor a cero
        raise aporte_periodico_menor_a_cero("ERROR: El aporte peridico debe ser mayor a 0")
    
    if aporte_periodico < 0: #Caso el aporte periodico no puede ser menor que cero 
        raise aporte_periodico_menor_a_cero("ERROR: El aporte periodico tiene que ser mayor a 0")
    
    if numero_periodos >60: #Caso el numero de periodods no puede pasar el limite de 60
        raise aporte_periodico_mayor_a_60("ERROR: el numero de periodos debe ser menor que 60")
    
    if tasa_interes < 0: #Caso de la tasa interes no puede ser negativa
        raise tasa_interes_negativa("ERROR: La tasa de interes no puede ser negativa")
    
    #En los mensajes de ERROR es lo que mostrara en pantalla en caso de que se capte un caso de esos 
    
    return monto_inicial * (1 + tasa_interes) ** numero_periodos + aporte_periodico * (((1 + tasa_interes) ** numero_periodos - 1) / tasa_interes) #Formula para sacar los resultados del ahorro

    