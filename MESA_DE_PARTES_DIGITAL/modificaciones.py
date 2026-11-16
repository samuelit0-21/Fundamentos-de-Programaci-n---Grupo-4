# MESA DE PARTES DIGITAL

from datos import expedientes
from almacenamiento import guardar_expedientes


def modificar_expediente():
    """Permite modificar los datos de un expediente."""

    print("\n--- MODIFICACION DE EXPEDIENTE ---")

    codigo = input("Ingrese el codigo del expediente: ").strip().upper()

    expediente_encontrado = None

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            expediente_encontrado = expediente
            break

    if expediente_encontrado is None:
        print("No se encontro el expediente.")
        return

    print("\n--- DATOS ACTUALES DEL EXPEDIENTE ---")
    print("Codigo:", expediente_encontrado["codigo"])
    print("Nombre:", expediente_encontrado["nombre"])
    print("DNI:", expediente_encontrado["dni"])
    print("Asunto:", expediente_encontrado["asunto"])

    print("\n--- INGRESE LOS NUEVOS DATOS ---")

    nombre = input("Nuevo nombre: ").strip()
    dni = input("Nuevo DNI: ").strip()
    asunto = input("Nuevo asunto: ").strip()

    if not nombre or not dni or not asunto:
        print("Todos los campos son obligatorios.")
        return

    if not dni.isdigit() or len(dni) != 8:
        print("El DNI debe tener exactamente 8 digitos.")
        return

    expediente_encontrado["nombre"] = nombre
    expediente_encontrado["dni"] = dni
    expediente_encontrado["asunto"] = asunto

    # Guardar los cambios permanentemente
    guardar_expedientes(expedientes)

    print("\nExpediente modificado correctamente.")
