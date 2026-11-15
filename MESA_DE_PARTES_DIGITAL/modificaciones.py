
# MESA DE PARTES DIGITAL

# Importamos la lista de expedientes
from datos import expedientes


def modificar_expediente():
    """Permite modificar los datos de un expediente."""

    print("\n--- MODIFICACION DE EXPEDIENTE ---")

    codigo = input("Ingrese el codigo del expediente: ").strip().upper()

    # Buscar el expediente por su codigo
    expediente_encontrado = None

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            expediente_encontrado = expediente
            break

    # Verificar si existe el expediente
    if expediente_encontrado is None:
        print("No se encontro el expediente.")
        return

    # Mostrar los datos actuales
    print("\n--- DATOS ACTUALES DEL EXPEDIENTE ---")
    print("Codigo:", expediente_encontrado["codigo"])
    print("Nombre:", expediente_encontrado["nombre"])
    print("DNI:", expediente_encontrado["dni"])
    print("Asunto:", expediente_encontrado["asunto"])

    # Solicitar los nuevos datos
    print("\n--- INGRESE LOS NUEVOS DATOS ---")

    nombre = input("Nuevo nombre: ").strip()
    dni = input("Nuevo DNI: ").strip()
    asunto = input("Nuevo asunto: ").strip()

    # Validar que los campos no esten vacios
    if not nombre or not dni or not asunto:
        print("Todos los campos son obligatorios.")
        return

    # Validar que el DNI tenga 8 digitos numericos
    if not dni.isdigit() or len(dni) != 8:
        print("El DNI debe tener exactamente 8 digitos.")
        return

    # Actualizar los datos del expediente
    expediente_encontrado["nombre"] = nombre
    expediente_encontrado["dni"] = dni
    expediente_encontrado["asunto"] = asunto

    print("\nExpediente modificado correctamente.")
