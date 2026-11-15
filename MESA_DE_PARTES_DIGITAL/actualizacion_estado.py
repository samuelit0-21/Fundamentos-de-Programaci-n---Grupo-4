# MESA DE PARTES DIGITAL

# Importamos la lista de expedientes
from datos import expedientes


def actualizar_estado():
    """Permite actualizar el estado de un expediente."""

    print("\n--- ACTUALIZACION DEL ESTADO DEL EXPEDIENTE ---")

    # Solicitar el codigo del expediente
    codigo = input("Ingrese el codigo del expediente: ").strip().upper()

    # Buscar el expediente en la lista
    expediente_encontrado = None

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            expediente_encontrado = expediente
            break

    # Verificar que el expediente exista
    if expediente_encontrado is None:
        print("No se encontro el expediente.")
        return

    # Mostrar el estado actual
    print("\nEstado actual:", expediente_encontrado.get("estado", "Pendiente"))

    # Mostrar las opciones disponibles
    print("\nSeleccione el nuevo estado:")
    print("1. Pendiente")
    print("2. En proceso")
    print("3. Atendido")

    opcion = input("Seleccione una opcion: ").strip()

    # Diccionario de estados disponibles
    estados = {
        "1": "Pendiente",
        "2": "En proceso",
        "3": "Atendido"
    }

    # Validar la opcion seleccionada
    if opcion not in estados:
        print("Opcion de estado no valida.")
        return

    # Actualizar el estado del expediente
    expediente_encontrado["estado"] = estados[opcion]

    print("\nEstado actualizado correctamente.")
    print("Nuevo estado:", expediente_encontrado["estado"])
