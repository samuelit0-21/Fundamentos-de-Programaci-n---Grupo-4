
# MESA DE PARTES DIGITAL

# Importamos las funciones de los diferentes módulos
from registros import registrar_expediente
from consultas import (
    buscar_expediente,
    buscar_por_dni,
    mostrar_expedientes,
    buscar_por_nombre
)
from ordenamiento import ordenar_expedientes_por_fecha
from modificaciones import modificar_expediente
from eliminaciones import eliminar_expediente
from actualizacion_estado import actualizar_estado

# Importamos la lista de expedientes
from datos import expedientes

# Importamos las cuentas de trabajadores
from trabajadores import trabajadores

# Importamos el acceso del ciudadano
from acceso_ciudadano import iniciar_sesion_ciudadanos

def mostrar_menu_inicial():
    """Muestra el menú inicial del programa."""

    print("\n====================================")
    print("       MESA DE PARTES DIGITAL")
    print("====================================")
    print("1. Acceso de trabajador")
    print("2. Acceso ciudadano")
    print("3. Salir")
    print("====================================")

def validar_credenciales(correo, contrasena):
    """Comprueba las credenciales del trabajador."""

    if correo in trabajadores:
        if trabajadores[correo]["contrasena"] == contrasena:
            return True

    return False


def mostrar_acceso_trabajador():
    """Solicita y valida el acceso del trabajador."""

    print("\n====================================")
    print("       ACCESO DE TRABAJADORES")
    print("====================================")

    correo = input("Ingrese su correo electrónico: ").strip()
    contrasena = input("Ingrese su contraseña: ").strip()

    if validar_credenciales(correo, contrasena):

        nombre = trabajadores[correo]["nombre"]

        print("\n====================================")
        print("       ¡ACCESO AUTORIZADO!")
        print("====================================")
        print(f"Bienvenido, {nombre}.")
        print("====================================")

        return True

    else:
        print("\n====================================")
        print("       ACCESO DENEGADO")
        print("====================================")
        print("Correo o contraseña incorrectos.")
        print("Verifique sus datos e intente nuevamente.")
        print("====================================")

        return False



def mostrar_menu_trabajador():
    """Muestra el menú exclusivo del trabajador."""

    print("\n====================================")
    print("       MENÚ DEL TRABAJADOR")
    print("====================================")
    print("1. Registrar expediente")
    print("2. Buscar expediente por código")
    print("3. Ordenar expedientes por fecha")
    print("4. Buscar expediente por nombre")
    print("5. Mostrar todos los expedientes")
    print("6. Buscar expediente por DNI")
    print("7. Modificar datos del expediente")
    print("8. Eliminar expediente")
    print("9. Actualizar estado del expediente")
    print("10. Cerrar sesión")
    print("====================================")


def menu():
    """Controla el acceso inicial al programa."""

    while True:
        mostrar_menu_inicial()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":

            acceso = mostrar_acceso_trabajador()

            if acceso:
                menu_administrativo()

        elif opcion == "2":
            print("\nGracias por utilizar Mesa de Partes Digital.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")

def menu():
    """Controla el acceso inicial al programa."""

    while True:
        mostrar_menu_inicial()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":

            acceso = mostrar_acceso_trabajador()

            if acceso:
                menu_administrativo()

        elif opcion == "2":
            iniciar_sesion_ciudadanos()

        elif opcion == "3":
            print("\nGracias por utilizar Mesa de Partes Digital.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")

def menu_administrativo():
    """Controla las opciones exclusivas del trabajador."""

    while True:
        mostrar_menu_trabajador()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_expediente()

        elif opcion == "2":
            buscar_expediente()

        elif opcion == "3":
            ordenar_expedientes_por_fecha(expedientes)

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
            print("\nSesión cerrada correctamente.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
