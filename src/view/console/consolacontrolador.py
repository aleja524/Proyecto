import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from controller.usuario_controlador import (
    conectar_db, agregar_usuario, agregar_calculadora_ahorro, consultar_usuario_con_ahorros,
    agregar_detalle_ahorro, eliminar_usuario, eliminar_ahorro
)

def main_menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar usuario")
        print("2. Agregar ahorro")
        print("3. Consultar usuario y sus ahorros")
        print("4. Eliminar usuario")
        print("5. Eliminar ahorro de usuario")
        print("6. Salir")

        try:
            opcion = int(input("Selecciona una opción (1-6): "))
        except ValueError:
            print(" Opción inválida. Ingresa un número entre 1 y 6.")
            continue

        if opcion == 1:
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            documento_identidad = input("Documento de identidad: ").strip()
            correo = input("Correo electrónico: ").strip()
            telefono = input("Teléfono: ").strip()
            agregar_usuario(nombre, apellido, documento_identidad, correo, telefono)

        elif opcion == 2:
            try:
                id_usuario = int(input("ID del usuario: "))
                monto_mensual = float(input("Monto mensual: "))
                meses = int(input("Cantidad de meses: "))
                tasa_interes = float(input("Tasa de interés (ej: 0.05 para 5%): "))
                total_ahorrado = monto_mensual * meses * (1 + tasa_interes)
            except ValueError:
                print(" Datos inválidos. Verifica e intenta de nuevo.")
                continue

            agregar_calculadora_ahorro(id_usuario, monto_mensual, meses, tasa_interes, total_ahorrado)

            # Opción adicional: ¿Deseas agregar detalles mes a mes?
            agregar_detalles = input("¿Deseas agregar detalles de ahorro mes a mes? (s/n): ").strip().lower()
            if agregar_detalles == 's':
                for mes in range(1, meses + 1):
                    monto = monto_mensual * mes * (1 + tasa_interes)
                    agregar_detalle_ahorro(id_usuario, mes, monto)

        elif opcion == 3:
            try:
                id_usuario = int(input("ID del usuario a consultar: "))
                consultar_usuario_con_ahorros(id_usuario)
            except ValueError:
                print(" ID inválido.")
                continue

        elif opcion == 4:
            try:
                id_usuario = int(input("ID del usuario a eliminar: "))
                confirm = input(f" ¿Estás seguro que deseas eliminar al usuario {id_usuario}? (s/n): ").lower()
                if confirm == 's':
                    eliminar_usuario(id_usuario)
                    print(" Usuario eliminado.")
                else:
                    print("Operación cancelada.")
            except ValueError:
                print(" ID inválido.")
                continue

        elif opcion == 5:
            try:
                id_usuario = int(input("ID del usuario cuyos ahorros deseas eliminar: "))
                confirm = input(f" Esto eliminará TODOS los ahorros del usuario {id_usuario}. ¿Continuar? (s/n): ").lower()
                if confirm == 's':
                    eliminar_ahorro(id_usuario)
                    print(" Ahorros eliminados.")
                else:
                    print("Operación cancelada.")
            except ValueError:
                print(" ID inválido.")
                continue

        elif opcion == 6:
            print(" Saliendo del programa...")
            break

        else:
            print(" Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main_menu()
