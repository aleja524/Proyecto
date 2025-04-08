class ErrorFaltaDeDatos(Exception):
    pass

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
