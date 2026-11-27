
# MESA DE PARTES DIGITAL

# Importamos las funciones de los diferentes módulos
from registros import registrar_expediente
from consultas import buscar_expediente, buscar_por_dni, mostrar_expedientes
from ordenamiento import ordenar_expedientes
from modificaciones import modificar_expediente
from eliminaciones import eliminar_expediente
from actualizacion_estado import actualizar_estado
from consultas import buscar_por_nombre
from trabajadores import trabajadores


def mostrar_acceso_trabajador():
    """Solicita los datos de acceso del trabajador."""

    print("\n====================================")
    print("       ACCESO DE TRABAJADORES")
    print("====================================")

    correo = input("Ingrese su correo electrónico: ").strip()
    contrasena = input("Ingrese su contraseña: ").strip()

    print("\nDatos de acceso ingresados correctamente.")


def menu():
    """Muestra el menú principal del programa."""

    while True:
        print("\n====================================")
        print("       MESA DE PARTES DIGITAL")
        print("====================================")
        print("1. Acceso de trabajador")
        print("2. Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            mostrar_acceso_trabajador()

        elif opcion == "2":
            print("\nGracias por utilizar Mesa de Partes Digital.")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    menu()

