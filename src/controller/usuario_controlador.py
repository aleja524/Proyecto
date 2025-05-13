import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import psycopg2
import SecretConfig
from src.model.usuar import *



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

  
    def CrearTabla():
        """
        Crea la tabla de usuarios desde archivo SQL
        """
        cursor = ControladorUsuarios.ObtenerCursor()
        with open("sql/crear_usuarios.sql", "r") as file:
            cursor.execute(file.read())
        cursor.connection.commit()


    def EliminarTabla():
        """
        Elimina la tabla de usuarios desde archivo SQL
        """
        cursor = ControladorUsuarios.ObtenerCursor()
        with open("sql/eliminar_usuarios.sql", "r") as file:
            cursor.execute(file.read())
        cursor.connection.commit()


    def InsertarUsuario(usuario: Usuario):
        """
        Inserta un objeto Usuario en la base de datos
        """
        cursor = ControladorUsuarios.ObtenerCursor()
        cursor.execute("""
            INSERT INTO usuarios (
                nombre, apellido, documeto_identidad, correo, telefono
            ) VALUES (%s, %s, %s, %s, %s)
        """, (
            usuario.nombre,
            usuario.apellido,
            usuario.documento_identidad,
            usuario.correo,
            usuario.telefono
        ))
        cursor.connection.commit()


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
   
ControladorUsuarios.CrearTabla()