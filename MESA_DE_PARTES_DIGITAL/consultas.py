
# MESA DE PARTES DIGITAL

# Importamos la lista de expedientes
from datos import expedientes


def buscar_expediente():
    """Busca un expediente mediante su codigo."""

    print("\n--- BUSQUEDA POR CODIGO ---")

    codigo = input("Ingrese el codigo del expediente: ")

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print("\nExpediente encontrado:")
            print("Codigo:", expediente["codigo"])
            print("Nombre:", expediente["nombre"])
            print("DNI:", expediente["dni"])
            print("Asunto:", expediente["asunto"])
            print("Estado:", expediente["estado"])
            return

    print("No se encontro el expediente.")


def buscar_por_dni():
    """Busca expedientes mediante el DNI del solicitante."""

    print("\n--- BUSQUEDA POR DNI ---")

    dni = input("Ingrese el DNI: ")

    if not dni.isdigit() or len(dni) != 8:
        print("El DNI debe tener exactamente 8 digitos.")
        return

    encontrados = False

    for expediente in expedientes:
        if expediente["dni"] == dni:
            print("\nExpediente encontrado:")
            print("Codigo:", expediente["codigo"])
            print("Nombre:", expediente["nombre"])
            print("Asunto:", expediente["asunto"])
            print("Estado:", expediente["estado"])
            encontrados = True

    if not encontrados:
        print("No existen expedientes asociados a ese DNI.")


def mostrar_expedientes():
    """Muestra todos los expedientes registrados."""

    print("\n--- LISTA DE EXPEDIENTES ---")

    if not expedientes:
        print("No hay expedientes registrados.")
        return

    for expediente in expedientes:
        print("-------------------------")
        print("Codigo:", expediente["codigo"])
        print("Nombre:", expediente["nombre"])
        print("DNI:", expediente["dni"])
        print("Asunto:", expediente["asunto"])
        print("Estado:", expediente["estado"])
