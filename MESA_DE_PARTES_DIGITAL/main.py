
# MESA DE PARTES DIGITAL

# Importamos las funciones de los diferentes modulos
from registros import registrar_expediente
from consultas import buscar_expediente, mostrar_expedientes
from ordenamiento import ordenar_expedientes


def mostrar_menu():
    """Muestra las opciones del menu principal."""

    print("\n====================================")
    print("       MESA DE PARTES DIGITAL")
    print("====================================")
    print("1. Registrar expediente")
    print("2. Buscar expediente por codigo")
    print("3. Ordenar expedientes por codigo")
    print("4. Mostrar todos los expedientes")
    print("5. Salir")
    print("====================================")


def menu():
    """Controla las opciones del programa."""

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_expediente()

        elif opcion == "2":
            buscar_expediente()

        elif opcion == "3":
            ordenar_expedientes()

        elif opcion == "4":
            mostrar_expedientes()

        elif opcion == "5":
            print("\nGracias por utilizar Mesa de Partes Digital.")
            break

        else:
            print("\nOpcion no valida. Intente nuevamente.")


# Ejecutar el programa principal
if __name__ == "__main__":
    menu()
