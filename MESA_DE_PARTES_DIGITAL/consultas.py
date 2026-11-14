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
            print("Estado:", expediente["estado"])
            return

    print("No se encontro el expediente.")

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
