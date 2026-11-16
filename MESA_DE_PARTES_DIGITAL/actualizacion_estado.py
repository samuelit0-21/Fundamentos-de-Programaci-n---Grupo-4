
# MESA DE PARTES DIGITAL

from datos import expedientes
from almacenamiento import guardar_expedientes


def actualizar_estado():
    """Permite actualizar el estado de un expediente."""

    print("\n--- ACTUALIZACION DEL ESTADO DEL EXPEDIENTE ---")

    codigo = input("Ingrese el codigo del expediente: ").strip().upper()

    expediente_encontrado = None

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            expediente_encontrado = expediente
            break

    if expediente_encontrado is None:
        print("No se encontro el expediente.")
        return

    print("\nEstado actual:", expediente_encontrado.get("estado", "Pendiente"))

    print("\nSeleccione el nuevo estado:")
    print("1. Pendiente")
    print("2. En proceso")
    print("3. Atendido")

    opcion = input("Seleccione una opcion: ").strip()

    estados = {
        "1": "Pendiente",
        "2": "En proceso",
        "3": "Atendido"
    }

    if opcion not in estados:
        print("Opcion de estado no valida.")
        return

    expediente_encontrado["estado"] = estados[opcion]

    # Guardar permanentemente el cambio de estado
    guardar_expedientes(expedientes)

    print("\nEstado actualizado correctamente.")
    print("Nuevo estado:", expediente_encontrado["estado"])
