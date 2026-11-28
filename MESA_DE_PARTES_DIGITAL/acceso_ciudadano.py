# MESA DE PARTES DIGITAL
# Módulo de acceso para el ciudadano

from registros import registrar_expediente
from datos import expedientes


def consultar_mis_expedientes(dni):
    """Muestra únicamente los expedientes asociados al DNI del ciudadano."""
    print(f"\n--- MIS EXPEDIENTES (DNI: {dni}) ---")

    encontrado = False

    for expediente in expedientes:
        if expediente["dni"] == dni:
            print("-------------------------")
            print("Código:", expediente["codigo"])
            print("Nombre:", expediente["nombre"])
            print("DNI:", expediente["dni"])
            print("Asunto:", expediente["asunto"])
            print("Fecha de ingreso:", expediente.get("fecha_ingreso", "No registrada"))
            print("Estado:", expediente.get("estado", "Pendiente"))
            encontrado = True

    if not encontrado:
        print("No se encontraron expedientes asociados a su DNI.")


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
            consultar_mis_expedientes(dni)

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

    if not dni.isdigit() or len(dni) != 8:
        print("Error: El DNI debe tener exactamente 8 dígitos numéricos.")
        return

    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return

    print("\nDatos validados correctamente.")
    menu_ciudadano(dni, nombre)
