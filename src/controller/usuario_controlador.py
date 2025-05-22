import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import psycopg2
import SecretConfig
from src.model.usuar import *

def conectar_db():
    """
    Función auxiliar para tests: intenta conectar usando SecretConfig y devuelve la conexión o None.
    """
    try:
        conn = psycopg2.connect(
            host=SecretConfig.PGHOST,
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD
        )
        conn.autocommit = True
        return conn
    except Exception:
        return None

class ControladorUsuarios:
    """
    Controlador encargado de gestionar los usuarios
    """

   
    def ObtenerCursor():
        """
        Crea la conexión y retorna un cursor
        """
        conexion = psycopg2.connect(
            host=SecretConfig.PGHOST,
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD
        )
        return conexion.cursor()

    @staticmethod
    def CrearTabla():
        """
        Crea la tabla de usuarios desde archivo SQL
        """
        cursor = ControladorUsuarios.ObtenerCursor()
        with open("sql/crear_usuarios.sql", "r") as file:
            cursor.execute(file.read())
        cursor.connection.commit()

    @staticmethod
    def EliminarTabla():
        """
        Elimina la tabla de usuarios desde archivo SQL
        """
        cursor = ControladorUsuarios.ObtenerCursor()
        with open("sql/eliminar_usuarios.sql", "r") as file:
            cursor.execute(file.read())
        cursor.connection.commit()

    @staticmethod
    def InsertarUsuario(usuario: Usuario):
        """
        Inserta un objeto Usuario en la base de datos
        """
        cursor = ControladorUsuarios.ObtenerCursor()
        cursor.execute("""
            INSERT INTO usuarios (
                nombre, apellido, documento_identidad, correo, telefono
            ) VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (documento_identidad) DO NOTHING                     
        """, (
            usuario.nombre,
            usuario.apellido,
            usuario.documento_identidad,
            usuario.correo,
            usuario.telefono
        ))
        cursor.connection.commit()


    @staticmethod
    def EliminarUsuarioPorDocumento(documento_identidad: int):
        """
        Elimina un usuario de la base de datos según su documento de identidad.
        """
        cursor = ControladorUsuarios.ObtenerCursor()
        cursor.execute("""
            DELETE FROM usuarios WHERE documento_identidad = %s
        """, (documento_identidad,))
        cursor.connection.commit()
    


    @staticmethod
    def BuscarUsuarioPorDocumento(documento_identidad: int):
        """
        Busca un usuario por su documento de identidad
        """
        cursor = ControladorUsuarios.ObtenerCursor()
        cursor.execute("""
            SELECT nombre, apellido, documento_identidad, correo, telefono
            FROM usuarios
            WHERE documento_identidad = %s
        """, (documento_identidad,))
        fila = cursor.fetchone()

        if fila:
            return Usuario(*fila)
        return None



