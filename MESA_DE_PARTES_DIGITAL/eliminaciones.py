# MESA DE PARTES DIGITAL

from datos import expedientes
from almacenamiento import guardar_expedientes


def eliminar_expediente():
    """Permite eliminar un expediente registrado."""

    print("\n--- ELIMINACION DE EXPEDIENTE ---")

    codigo = input("Ingrese el codigo del expediente: ").strip().upper()

    expediente_encontrado = None

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            expediente_encontrado = expediente
            break

    if expediente_encontrado is None:
        print("No se encontro el expediente.")
        return

    print("\n--- DATOS DEL EXPEDIENTE ---")
    print("Codigo:", expediente_encontrado["codigo"])
    print("Nombre:", expediente_encontrado["nombre"])
    print("DNI:", expediente_encontrado["dni"])
    print("Asunto:", expediente_encontrado["asunto"])

    confirmacion = input(
        "\n¿Esta seguro de eliminar este expediente? (S/N): "
    ).strip().upper()

    if confirmacion == "S":
        expedientes.remove(expediente_encontrado)

        # Guardar los cambios en el archivo JSON
        guardar_expedientes(expedientes)

        print("Expediente eliminado correctamente.")

    elif confirmacion == "N":
        print("Se cancelo la eliminacion del expediente.")

    else:
        print("Opcion no valida. No se elimino el expediente.")
