
# MESA DE PARTES DIGITAL

# Importamos la lista de expedientes
from datos import expedientes


def ordenar_expedientes():
    """Ordena los expedientes por codigo de manera ascendente."""

    print("\n--- ORDENAMIENTO DE EXPEDIENTES ---")

    if not expedientes:
        print("No hay expedientes para ordenar.")
        return

    # Aplicar el metodo de burbuja
    n = len(expedientes)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if expedientes[j]["codigo"] > expedientes[j + 1]["codigo"]:
                expedientes[j], expedientes[j + 1] = expedientes[j + 1], expedientes[j]

    print("Expedientes ordenados correctamente.")

    # Mostrar los expedientes ordenados
    for expediente in expedientes:
        print("-------------------------")
        print("Codigo:", expediente["codigo"])
        print("Nombre:", expediente["nombre"])
        print("DNI:", expediente["dni"])
        print("Asunto:", expediente["asunto"])
