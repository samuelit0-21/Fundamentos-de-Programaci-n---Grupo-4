# MESA DE PARTES DIGITAL

# Importamos la lista de expedientes
from datos import expedientes


def eliminar_expediente():
    """Permite eliminar un expediente registrado."""

    print("\n--- ELIMINACION DE EXPEDIENTE ---")

    # Solicitar el codigo del expediente
    codigo = input("Ingrese el codigo del expediente: ").strip().upper()

    # Buscar el expediente en la lista
    expediente_encontrado = None

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            expediente_encontrado = expediente
            break

    # Verificar si el expediente existe
    if expediente_encontrado is None:
        print("No se encontro el expediente.")
        return

    # Mostrar los datos del expediente encontrado
    print("\n--- DATOS DEL EXPEDIENTE ---")
    print("Codigo:", expediente_encontrado["codigo"])
    print("Nombre:", expediente_encontrado["nombre"])
    print("DNI:", expediente_encontrado["dni"])
    print("Asunto:", expediente_encontrado["asunto"])

    # Solicitar confirmacion antes de eliminar
    confirmacion = input(
        "\n¿Esta seguro de eliminar este expediente? (S/N): "
    ).strip().upper()

    # Eliminar o cancelar la operacion
    if confirmacion == "S":
        expedientes.remove(expediente_encontrado)
        print("Expediente eliminado correctamente.")

    elif confirmacion == "N":
        print("Se cancelo la eliminacion del expediente.")

    else:
        print("Opcion no valida. No se elimino el expediente.")
