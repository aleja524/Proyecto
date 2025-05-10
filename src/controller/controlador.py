import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import psycopg2
import SecretConfig


#Conectar la base de datos 
#Este método se encarga de conectar a la base de datos.
#Se le pasa el host, la base de datos, el usuario y la contraseña.
#Si no se puede conectar, devuelve None.
#Si se conecta, devuelve la conexión.
def conectar_db():
    try:
        conn = psycopg2.connect(
            host=SecretConfig.PGHOST,
            database=SecretConfig.PGDATABASE,
            user=SecretConfig.PGUSER,
            password=SecretConfig.PGPASSWORD
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        return None 


#Este método se encarga de agregar un nuevo usuario a la base de datos.
#Se le pasa el nombre, apellido, documento de identidad, correo electrónico y teléfono.
def agregar_usuario(nombre, apellido, documento_identidad, correo_electronico, telefono):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = """
                INSERT INTO usuarios (nombre, apellido, documento_identidad, correo_electronico, telefono)
                VALUES (%s, %s, %s, %s, %s)
                """
                cur.execute(sql, (nombre, apellido, documento_identidad, correo_electronico, telefono))
                conn.commit()
            conn.close()
            print("Usuario agregado exitosamente.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error al agregar el usuario: {error}")


#Este método se encarga de agregar un nuevo ahorro a la base de datos.
#Se le pasa el id del usuario, el monto mensual, los meses, la tasa de interes y el total ahorrado.
def agregar_calculadora_ahorro(id_usuario, monto_mensual, meses, tasa_interes, total_ahorrado):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = """
                INSERT INTO calculadora_ahorro (id_usuario, monto_mensual, meses, tasa_interes, total_ahorrado)
                VALUES (%s, %s, %s, %s, %s)
                """
                cur.execute(sql, (id_usuario, monto_mensual, meses, tasa_interes, total_ahorrado))
                conn.commit()
            conn.close()
            print("Ahorro registrado exitosamente.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error al registrar ahorro: {error}")


#Este método se encarga de agregar un detalle de ahorro a la base de datos.
#Se le pasa el id del ahorro, el mes y el monto acumulado.
def agregar_detalle_ahorro(ahorro_id, mes, monto_acumulado):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = """
                INSERT INTO detalles_ahorro (ahorro_id, mes, monto_acumulado)
                VALUES (%s, %s, %s)
                """
                cur.execute(sql, (ahorro_id, mes, monto_acumulado))
                conn.commit()
            conn.close()
            print("Detalle de ahorro agregado.")
    except (Exception, psycopg2.Error) as error:
        print(f"Error al agregar detalle de ahorro: {error}")


#Este método se encarga de consultar un usuario y sus ahorros.
#Se le pasa el id del usuario.
#Primero consulta el usuario y luego consulta los ahorros del usuario.
def consultar_usuario_con_ahorros(id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                # Usuario
                cur.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
                usuario = cur.fetchone()

                if not usuario:
                    print("Usuario no encontrado.")
                    return
                
                print("Datos del usuario:")
                print(usuario)

                # Ahorros del usuario
                cur.execute("SELECT * FROM calculadora_ahorro WHERE usuario_id = %s", (id_usuario,))
                ahorros = cur.fetchall()

                for ahorro in ahorros:
                    print("\nAhorro:")
                    print(ahorro)

                    ahorro_id = ahorro[0]
                    cur.execute("SELECT * FROM detalles_ahorro WHERE ahorro_id = %s", (ahorro_id,))
                    detalles = cur.fetchall()

                    for detalle in detalles:
                        print(" - Detalle: ", detalle)

            conn.close()
    except (Exception, psycopg2.Error) as error:
        print(f"Error al consultar datos: {error}")



# Función para eliminar un usuario
def eliminar_usuario(id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "DELETE FROM usuarios WHERE id_Usuarios = %s"
                cur.execute(sql, (id_usuario,))
                conn.commit()
            conn.close()
    except (Exception, psycopg2.Error) as error:
        print(f"Error al eliminar el usuario: {error}")

# Función para eliminar los datos de la tabla de liquidación
def eliminar_ahorro(id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "DELETE FROM ahorro WHERE ID_Usuarios = %s"
                cur.execute(sql, (id_usuario,))
                conn.commit()
            conn.close()
    except (Exception, psycopg2.Error) as error:
        print(f"Error al eliminar los datos del ahorro: {error}")


        