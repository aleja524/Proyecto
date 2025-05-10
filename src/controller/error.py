from controller.controlador import conectar_db
import psycopg2

# Decorador para manejar errores
def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (Exception, psycopg2.Error) as error:
            print(f"Error en la función {func.__name__}: {error}")
            conn = conectar_db()
            if conn:
                conn.rollback()
                conn.close()
    return wrapper


# Función para agregar un usuario
# Esta función agrega un usuario a la base de datos.
# Se utiliza un decorador para manejar errores.
@handle_error
def agregar_usuario(nombre, apellido, documento_identidad, correo_electronico, telefono):
    conn = conectar_db()
    if conn:
        with conn.cursor() as cur:
            sql = """
                INSERT INTO usuarios (nombre, apellido, documento_identidad, correo_electronico, telefono)
                VALUES (%s, %s, %s, %s, %s)
            """
            cur.execute(sql, (nombre, apellido, documento_identidad, correo_electronico, telefono))
            conn.commit()
            print("Usuario agregado correctamente.")
        conn.close()



# Función para agregar un ahorro
# Esta función agrega un ahorro a la base de datos.
# Se utiliza un decorador para manejar errores.
@handle_error
def agregar_ahorro(usuario_id, monto_mensual, meses, tasa_interes, total_ahorrado):
    conn = conectar_db()
    if conn:
        with conn.cursor() as cur:
            sql = """
                INSERT INTO calculadora_ahorro (usuario_id, monto_mensual, meses, tasa_interes, total_ahorrado)
                VALUES (%s, %s, %s, %s, %s)
            """
            cur.execute(sql, (usuario_id, monto_mensual, meses, tasa_interes, total_ahorrado))
            conn.commit()
            print("Ahorro registrado correctamente.")
        conn.close()


# Función para agregar un detalle de ahorro
# Esta función agrega un detalle de ahorro a la base de datos.
# Se utiliza un decorador para manejar errores.
@handle_error
def agregar_detalle_ahorro(ahorro_id, mes, monto_acumulado):
    conn = conectar_db()
    if conn:
        with conn.cursor() as cur:
            sql = """
                INSERT INTO detalles_ahorro (ahorro_id, mes, monto_acumulado)
                VALUES (%s, %s, %s)
            """
            cur.execute(sql, (ahorro_id, mes, monto_acumulado))
            conn.commit()
            print("Detalle de ahorro agregado correctamente.")
        conn.close()




## Función para consultar un usuario por ID
# Esta función consulta un usuario y sus ahorros en la base de datos.
# Se utiliza un decorador para manejar errores.
@handle_error
def consultar_usuario(id_usuario):
    conn = conectar_db()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            usuario = cur.fetchone()

            if not usuario:
                print("Usuario no encontrado.")
                return

            print("Datos del usuario:")
            print("ID:", usuario[0])
            print("Nombre:", usuario[1], usuario[2])
            print("Documento:", usuario[3])
            print("Correo:", usuario[4])
            print("Teléfono:", usuario[5])

            cur.execute("SELECT * FROM calculadora_ahorro WHERE usuario_id = %s", (id_usuario,))
            ahorros = cur.fetchall()

            for ahorro in ahorros:
                print("\nAhorro ID:", ahorro[0])
                print("Monto mensual:", ahorro[2])
                print("Meses:", ahorro[3])
                print("Tasa de interés:", ahorro[4])
                print("Total ahorrado:", ahorro[5])

                cur.execute("SELECT * FROM detalles_ahorro WHERE ahorro_id = %s", (ahorro[0],))
                detalles = cur.fetchall()

                for detalle in detalles:
                    print(f"  Mes {detalle[2]} → Acumulado: ${detalle[3]:,.2f}")

        conn.close()



# Función para eliminar un usuario
# Esta función elimina un usuario de la base de datos.
# Se utiliza un decorador para manejar errores.
@handle_error
def eliminar_usuario(id_usuario):
    conn = conectar_db()
    if conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            conn.commit()
            print("Usuario eliminado correctamente.")
        conn.close()
