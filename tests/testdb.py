import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Agregar ruta al src para importar el controlador correctamente
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.append(src_dir)

from controller.controlador import conectar_db
from controller.error import agregar_usuario, agregar_ahorro, consultar_usuario, eliminar_usuario
import SecretConfig

class TestConsultarUsuario(unittest.TestCase):
    def test_consultar_usuario_existente(self):
        id_usuario = 1
        consultar_usuario(id_usuario)
        # Nota: Esta prueba solo imprime, no afirma nada. Puedes agregar asserts si usas return en vez de print.

class TestEliminarUsuario(unittest.TestCase):
    def test_eliminar_usuario(self):
        id_usuario = 1
        eliminar_usuario(id_usuario)
        # Similarmente, esto solo verifica que no lance error.

class TestConectarDBError(unittest.TestCase):
    def test_conectar_db_error(self):
        # Guardamos valor original
        original_pg_host = SecretConfig.PGHOST
        SecretConfig.PGHOST = "invalid_host"

        conn = conectar_db()
        self.assertIsNone(conn)

        # Restauramos para que no afecte otras pruebas
        SecretConfig.PGHOST = original_pg_host

class TestConsultarUsuarioNoExistente(unittest.TestCase):
    def test_consultar_usuario_no_existente(self):
        id_usuario = 99999  # ID probablemente inexistente
        consultar_usuario(id_usuario)

class TestAgregarUsuario(unittest.TestCase):
    def test_agregar_usuario(self):
        agregar_usuario("Juan", "Pérez", "123456789", "juan@example.com", "3100000000")

class TestAgregarAhorro(unittest.TestCase):
    def test_agregar_ahorro(self):
        usuario_id = 1  # Asegúrate que este ID exista para no causar error de FK
        agregar_ahorro(usuario_id, 100000, 12, 0.03, 123456)

if __name__ == '__main__':
    unittest.main()
