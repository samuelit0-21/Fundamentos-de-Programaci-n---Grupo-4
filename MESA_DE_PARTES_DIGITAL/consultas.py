# MESA DE PARTES DIGITAL

# Importamos la lista de expedientes
from datos import expedientes


def buscar_expediente():
    """Busca un expediente mediante su codigo."""

    print("\n--- BUSQUEDA POR CODIGO ---")

    codigo = input("Ingrese el codigo del expediente: ").strip().upper()

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print("\nExpediente encontrado:")
            print("Codigo:", expediente["codigo"])
            print("Nombre:", expediente["nombre"])
            print("DNI:", expediente["dni"])
            print("Asunto:", expediente["asunto"])
            print("Estado:", expediente.get("estado", "Pendiente"))
            return

    print("No se encontro el expediente.")


def buscar_por_dni():
    """Busca expedientes mediante el DNI del solicitante."""

    print("\n--- BUSQUEDA POR DNI ---")

    dni = input("Ingrese el DNI del solicitante: ").strip()

    if not dni.isdigit() or len(dni) != 8:
        print("El DNI debe tener exactamente 8 digitos numericos.")
        return

    encontrado = False

    for expediente in expedientes:
        if expediente["dni"] == dni:
            print("\nExpediente encontrado:")
            print("Codigo:", expediente["codigo"])
            print("Nombre:", expediente["nombre"])
            print("DNI:", expediente["dni"])
            print("Asunto:", expediente["asunto"])
            print("Estado:", expediente.get("estado", "Pendiente"))
            encontrado = True

    if not encontrado:
        print("No se encontraron expedientes con ese DNI.")

def buscar_por_nombre():
    print("\n--- BUSCAR EXPEDIENTE POR NOMBRE ---")

    nombre_buscar = input("Ingrese el nombre del solicitante: ").strip()

    if not nombre_buscar:
        print("Error: debe ingresar un nombre.")
        return

    encontrado = False

    for expediente in expedientes:

        if nombre_buscar.lower() in expediente["nombre"].lower():

            print("\n--- EXPEDIENTE ENCONTRADO ---")
            print("Código:", expediente["codigo"])
            print("Nombre:", expediente["nombre"])
            print("DNI:", expediente["dni"])
            print("Asunto:", expediente["asunto"])
            print("Estado:", expediente["estado"])

            encontrado = True

    if not encontrado:
        print("No se encontraron expedientes con ese nombre.")


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
        print("Estado:", expediente.get("estado", "Pendiente"))
