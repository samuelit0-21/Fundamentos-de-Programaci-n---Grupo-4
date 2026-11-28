
# MESA DE PARTES DIGITAL

# Importamos la lista de expedientes
from datos import expedientes

# Ordenar expedientes por fecha de ingreso
def ordenar_expedientes_por_fecha(expedientes):

    # Verificar si existen expedientes
    if not expedientes:
        print("No existen expedientes registrados.")
        return
    
    # Verificar que los códigos sean únicos 
    if not verificar_codigos_unicos(expedientes):
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

# Verificar que los códigos de los expedientes sean únicos
def verificar_codigos_unicos(expedientes):

    codigos = []

    # Recorrer los expedientes registrados
    for expediente in expedientes:
        codigo = expediente["codigo"]

        # Comprobar si el código ya existe
        if codigo in codigos:
            print("Error: existen códigos duplicados.")
            return False

        codigos.append(codigo)

    # Confirmar que todos los códigos son únicos
    print("Todos los códigos son únicos.")
    return True

# Verificar que el ordenamiento no modifique los registros originales
def verificar_registros_originales(expedientes):

    # Crear una copia de los expedientes originales
    expedientes_originales = [expediente.copy() for expediente in expedientes]

    # Ordenar los expedientes por fecha
    expedientes_ordenados = sorted(
        expedientes,
        key=lambda expediente: expediente["fecha_ingreso"]
    )

    # Comparar los registros originales con los actuales
    if expedientes == expedientes_originales:
        print("Los registros originales se mantienen sin cambios.")
        return True

    print("Error: los registros originales fueron modificados.")
    return False


