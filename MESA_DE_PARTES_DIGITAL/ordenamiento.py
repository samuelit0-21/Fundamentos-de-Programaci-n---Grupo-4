
# MESA DE PARTES DIGITAL

# Importamos la lista de expedientes
from datos import expedientes

# Ordenar expedientes por fecha de ingreso
def ordenar_expedientes_por_fecha(expedientes):

    # Verificar si existen expedientes
    if not expedientes:
        print("No existen expedientes registrados.")
        return

    # Ordenar desde el más antiguo hasta el más reciente
    expedientes_ordenados = sorted(
        expedientes,
        key=lambda expediente: expediente["fecha_ingreso"]
    )

    # Mostrar los expedientes ordenados
    print("\n--- EXPEDIENTES ORDENADOS POR FECHA ---")

    for expediente in expedientes_ordenados:
        print("-----------------------------")
        print("Código:", expediente["codigo"])
        print("Nombre:", expediente["nombre"])
        print("DNI:", expediente["dni"])
        print("Asunto:", expediente["asunto"])
        print("Estado:", expediente["estado"])
        print("Fecha de ingreso:", expediente["fecha_ingreso"])

    return expedientes_ordenados


