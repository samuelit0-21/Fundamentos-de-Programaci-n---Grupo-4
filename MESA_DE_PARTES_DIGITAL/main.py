
# MESA DE PARTES DIGITAL

# Importamos las funciones de los diferentes módulos
from registros import registrar_expediente
from consultas import buscar_expediente, buscar_por_dni, mostrar_expedientes
from ordenamiento import ordenar_expedientes
from modificaciones import modificar_expediente
from eliminaciones import eliminar_expediente
from actualizacion_estado import actualizar_estado
from consultas import buscar_por_nombre


def mostrar_menu():
    """Muestra las opciones del menú principal."""

    print("\n====================================")
    print("       MESA DE PARTES DIGITAL")
    print("====================================")
    print("1. Registrar expediente")
    print("2. Buscar expediente por código")
    print("3. Ordenar expedientes por código")
    print("4. Buscar expediente por nombre")
    print("5. Mostrar todos los expedientes")
    print("6. Buscar expediente por DNI")
    print("7. Modificar datos del expediente")
    print("8. Eliminar expediente")
    print("9. Actualizar estado del expediente")
    print("10. Salir")
    print("====================================")


def menu():
    """Controla las opciones del programa."""

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_expediente()

        elif opcion == "2":
            buscar_expediente()

        elif opcion == "3":
            ordenar_expedientes()

        elif opcion == "4":
            buscar_por_nombre()

        elif opcion == "5":
            mostrar_expedientes()

        elif opcion == "6":
            buscar_por_dni()

        elif opcion == "7":
            modificar_expediente()

        elif opcion == "8":
            eliminar_expediente()

        elif opcion == "9":
            actualizar_estado()

        elif opcion == "10":
            print("\nGracias por utilizar Mesa de Partes Digital.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()

if _name_ == "_main_":
    menu()
