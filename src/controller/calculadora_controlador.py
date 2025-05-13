import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import psycopg2
import SecretConfig
from src.model.calculadora import CalculadoraAhorro

class ControladorCalculadora:

    @staticmethod
    def ObtenerCursor():
        conexion = psycopg2.connect(
            host=SecretConfig.PGHOST,
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD
        )
        return conexion.cursor()

    @staticmethod
    def CrearTabla():
        cursor = ControladorCalculadora.ObtenerCursor()
        with open("sql/crear_calculadora.sql", "r") as file:
            cursor.execute(file.read())
        cursor.connection.commit()

    @staticmethod
    def EliminarTabla():
        cursor = ControladorCalculadora.ObtenerCursor()
        with open("sql/eliminar_calculadora.sql", "r") as file:
            cursor.execute(file.read())
        cursor.connection.commit()

    @staticmethod
    def InsertarCalculadora(calc: CalculadoraAhorro):
        cursor = ControladorCalculadora.ObtenerCursor()
        cursor.execute("""
            INSERT INTO calculadora_ahorro (
                id_usuario, monto_mensual, meses, tasa_interes, total_ahorrado
            ) VALUES (%s, %s, %s, %s, %s)
        """, (
            calc.id_usuario,
            calc.monto_mensual,
            calc.meses,
            calc.tasa_interes,
            calc.total_ahorrado
        ))
        cursor.connection.commit()

    @staticmethod
    def BuscarCalculadoraPorUsuario(id_usuario: int):
        cursor = ControladorCalculadora.ObtenerCursor()
        cursor.execute("""
            SELECT id_usuario, monto_mensual, meses, tasa_interes, total_ahorrado, fecha_creacion
            FROM calculadora_ahorro
            WHERE id_usuario = %s
        """, (id_usuario,))
        fila = cursor.fetchone()
        if fila:
            return CalculadoraAhorro(*fila)
        return None




