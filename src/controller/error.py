import psycopg2
from SecretConfig import PGHOST, PGDATABASE, PGUSER, PGPASSWORD
from model.usuar import Usuario
from controller.usuario_controlador import ControladorUsuarios
from model.calculadora import CalculadoraAhorro
from controller.calculadora_controlador import ControladorCalculadora

def conectar_db():
    """
    Intenta conectar con la base de datos usando SecretConfig.
    """
    try:
        conn = psycopg2.connect(
            host=PGHOST,
            database=PGDATABASE,
            user=PGUSER,
            password=PGPASSWORD
        )
        conn.autocommit = True
        return conn
    except Exception:
        return None

def agregar_usuario(nombre, apellido, documento, correo, telefono):
    usuario = Usuario(nombre, apellido, int(documento), correo, telefono)
    ControladorUsuarios.InsertarUsuario(usuario)

def consultar_usuario(id_usuario):
    return ControladorUsuarios.BuscarUsuarioPorDocumento(id_usuario)

def eliminar_usuario(id_usuario):
    ControladorUsuarios.EliminarUsuarioPorDocumento(id_usuario)

def agregar_ahorro(usuario_id, monto_mensual, meses, tasa_interes, total_ahorrado):
    calc = CalculadoraAhorro(usuario_id, monto_mensual, meses, tasa_interes, total_ahorrado)
    ControladorCalculadora.InsertarCalculadora(calc)
