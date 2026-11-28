# MESA DE PARTES DIGITAL
# Módulo de acceso para el ciudadano

from registros import registrar_expediente


def menu_ciudadano(dni, nombre):
    """Muestra el menú exclusivo del ciudadano."""
    while True:
        print("\n====================================")
        print("         MENÚ CIUDADANO")
        print("====================================")
        print(f"Bienvenido, {nombre} (DNI: {dni})")
        print("1. Registrar nuevo expediente")
        print("2. Consultar mis expedientes")
        print("3. Cerrar sesión")
        print("====================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_expediente()

        elif opcion == "2":
            print("\n(Consulta por DNI pendiente de integración.)")

        elif opcion == "3":
            print("\nSesión de ciudadano cerrada. Regresando al menú principal.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


def iniciar_sesion_ciudadanos():
    """Solicita DNI y nombre del ciudadano y valida los datos."""
    print("\n--- ACCESO CIUDADANO ---")

    dni = input("Ingrese su DNI: ").strip()
    nombre = input("Ingrese su nombre completo: ").strip()

    # Validaciones
    if not dni.isdigit() or len(dni) != 8:
        print("Error: El DNI debe tener exactamente 8 dígitos numéricos.")
        return

    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    print("\nDatos validados correctamente.")
    menu_ciudadano(dni, nombre)
