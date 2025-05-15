import psycopg2 
import re
from datetime import datetime

# Configuración de la base de datos
DB_CONFIG = {
    "host": "ep-tiny-dream-a4pouibw-pooler.us-east-1.aws.neon.tech",
    "database": "neondb",
    "user": "neondb_owner",
    "password": "npg_AvHqTn5PojI0",
    "sslmode": "require"
}

class ConsolaControlador:
    def __init__(self):
        self.conn = None
        self.conectar_db()

    def conectar_db(self):
        try:
            self.conn = psycopg2.connect(**DB_CONFIG)
            self.conn.autocommit = True
            print("✅ Conexión a la base de datos exitosa")
        except Exception as e:
            print(f"❌ Error al conectar a la base de datos: {e}")
            exit()

    # ==================== CRUD USUARIOS ====================
    def crear_usuario(self):
        print("\n--- REGISTRAR NUEVO USUARIO ---")
        try:
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            documento = int(input("Documento de identidad: "))
            correo = input("Correo electrónico: ").strip()
            telefono = input("Teléfono: ").strip()

            if not self.validar_correo(correo):
                print("❌ Correo electrónico inválido")
                return

            if self.buscar_usuario(documento):
                print("❌ Ya existe un usuario con este documento")
                return

            with self.conn.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO usuarios 
                    (documento, telefono, nombre, apellido, correo) 
                    VALUES (%s, %s, %s, %s, %s)""",
                    (documento, telefono, nombre, apellido, correo)
                )
                print("✅ Usuario registrado exitosamente")

        except ValueError:
            print("❌ Documento debe ser numérico")
        except Exception as e:
            print(f"❌ Error al registrar usuario: {e}")

    def buscar_usuario(self, documento):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "SELECT documento, telefono, nombre, apellido, correo FROM usuarios WHERE documento = %s", 
                (documento,)
            )
            return cursor.fetchone()

    def actualizar_usuario(self):
        print("\n--- ACTUALIZAR DATOS DE USUARIO ---")
        try:
            documento = int(input("Documento del usuario a actualizar: "))
            usuario = self.buscar_usuario(documento)

            if not usuario:
                print("❌ Usuario no encontrado")
                return

            nuevo_nombre = input(f"Nuevo nombre ({usuario[2]}): ").strip() or usuario[2]
            nuevo_apellido = input(f"Nuevo apellido ({usuario[3]}): ").strip() or usuario[3]
            nuevo_correo = input(f"Nuevo correo ({usuario[4]}): ").strip() or usuario[4]
            nuevo_telefono = input(f"Nuevo teléfono ({usuario[1]}): ").strip() or usuario[1]

            if not self.validar_correo(nuevo_correo):
                print("❌ Correo electrónico inválido")
                return

            with self.conn.cursor() as cursor:
                cursor.execute(
                    """UPDATE usuarios 
                    SET nombre = %s, apellido = %s, correo = %s, telefono = %s 
                    WHERE documento = %s""",
                    (nuevo_nombre, nuevo_apellido, nuevo_correo, nuevo_telefono, documento)
                )
                print("✅ Datos del usuario actualizados correctamente")

        except ValueError:
            print("❌ Documento debe ser numérico")
        except Exception as e:
            print(f"❌ Error al actualizar usuario: {e}")

    def eliminar_usuario(self):
        print("\n--- ELIMINAR USUARIO ---")
        try:
            documento = int(input("Documento del usuario a eliminar: "))
            usuario = self.buscar_usuario(documento)

            if not usuario:
                print("❌ Usuario no encontrado")
                return

            confirmacion = input("¿Está seguro de eliminar este usuario y sus ahorros? (s/n): ").strip().lower()
            if confirmacion != 's':
                print("❌ Operación cancelada")
                return

            with self.conn.cursor() as cursor:
                cursor.execute("DELETE FROM calculadora_ahorro WHERE id_usuario = %s", (documento,))
                cursor.execute("DELETE FROM usuarios WHERE documento = %s", (documento,))
                print("✅ Usuario y sus ahorros eliminados exitosamente")

        except ValueError:
            print("❌ Documento debe ser numérico")
        except Exception as e:
            print(f"❌ Error al eliminar usuario: {e}")

    # ==================== CRUD AHORROS ====================
    def registrar_ahorro(self):
        print("\n--- REGISTRAR AHORRO ---")
        try:
            documento = int(input("Documento del usuario: "))
            usuario = self.buscar_usuario(documento)
            
            if not usuario:
                print("❌ Usuario no encontrado")
                return

            monto = float(input("Monto mensual a ahorrar: $"))
            meses = int(input("Duración (meses): "))
            tasa = float(input("Tasa de interés anual (ej. 5 para 5%): ")) / 100

            tasa_mensual = tasa / 12
            total_ahorrado = monto * (((1 + tasa_mensual) ** meses - 1) / tasa_mensual)

            with self.conn.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO calculadora_ahorro 
                    (id_usuario, monto_mensual, meses, tasa_interes, total_ahorrado, fecha_creacion) 
                    VALUES (%s, %s, %s, %s, %s, %s)""",
                    (documento, monto, meses, tasa, total_ahorrado, datetime.now())
                )
                print(f"✅ Ahorro registrado | Total proyectado: ${total_ahorrado:,.2f}")

        except ValueError:
            print("❌ Ingrese valores numéricos válidos")
        except Exception as e:
            print(f"❌ Error al registrar ahorro: {e}")

    # ==================== CONSULTAS ====================
    def consultar_usuario(self):
        try:
            documento = int(input("Documento del usuario: "))
            usuario = self.buscar_usuario(documento)
            
            if not usuario:
                print("❌ Usuario no encontrado")
                return

            print(f"\n👤 USUARIO: {usuario[2]} {usuario[3]} | DOC: {usuario[0]}")
            print(f"📧 Correo: {usuario[4]} | 📞 Teléfono: {usuario[1]}")

            with self.conn.cursor() as cursor:
                cursor.execute(
                    """SELECT monto_mensual, meses, tasa_interes, total_ahorrado, fecha_creacion 
                    FROM calculadora_ahorro WHERE id_usuario = %s""", 
                    (documento,)
                )
                ahorros = cursor.fetchall()

                if ahorros:
                    print("\n💰 PLANES DE AHORRO:")
                    for idx, ahorro in enumerate(ahorros, 1):
                        print(f"  {idx}. Monto mensual: ${ahorro[0]:,.2f}")
                        print(f"     Meses: {ahorro[1]} | Tasa anual: {ahorro[2]*100:.2f}%")
                        print(f"     Total proyectado: ${ahorro[3]:,.2f}")
                        print(f"     Fecha registro: {ahorro[4].strftime('%d/%m/%Y')}\n")
                else:
                    print("ℹ️ El usuario no tiene planes de ahorro registrados")

        except ValueError:
            print("❌ Documento debe ser numérico")
        except Exception as e:
            print(f"❌ Error al consultar: {e}")

    # ==================== FUNCIONES AUXILIARES ====================
    def validar_correo(self, correo):
        return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo) is not None

    # ==================== MENÚ PRINCIPAL ====================
    def mostrar_menu(self):
        while True:
            print("\n===== SISTEMA DE AHORROS =====")
            print("1. Registrar nuevo usuario")
            print("2. Registrar plan de ahorros")
            print("3. Consultar usuario y ahorros")
            print("4. Actualizar datos de usuario")
            print("5. Eliminar usuario")
            print("6. Salir")

            opcion = input("Seleccione una opción (1-6): ")

            if opcion == "1":
                self.crear_usuario()
            elif opcion == "2":
                self.registrar_ahorro()
            elif opcion == "3":
                self.consultar_usuario()
            elif opcion == "4":
                self.actualizar_usuario()
            elif opcion == "5":
                self.eliminar_usuario()
            elif opcion == "6":
                print("👋 ¡Hasta pronto!")
                if self.conn:
                    self.conn.close()
                break
            else:
                print("❌ Opción inválida")

if __name__ == "__main__":
    try:
        consola = ConsolaControlador()
        consola.mostrar_menu()
    except KeyboardInterrupt:
        print("\n👋 Programa terminado por el usuario.")
