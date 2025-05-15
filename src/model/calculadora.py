class CalculadoraAhorro:
    def __init__(self, id_usuario, monto_mensual, meses, tasa_interes, total_ahorrado, fecha_creacion=None):
        self.id_usuario = id_usuario
        self.monto_mensual = monto_mensual
        self.meses = meses
        self.tasa_interes = tasa_interes
        self.total_ahorrado = total_ahorrado
        self.fecha_creacion = fecha_creacion