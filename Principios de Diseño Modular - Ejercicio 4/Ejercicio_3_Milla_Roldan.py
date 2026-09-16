# Ejercicio 3 — Pipeline modular de datos
# Creamos una función encargada de obtener los datos.
# "fuente" representa de dónde provienen los datos.
def leer_datos(fuente):

    # Para este ejemplo simplemente devolvemos
    # una lista con números positivos y negativos.
    return [1, -2, 3, -4, 5]


# Creamos una función encargada de filtrar los datos.
def filtrar_positivos(datos):

    # Recorremos cada elemento "x" de la lista "datos".
    # Solamente conservamos aquellos que sean mayores que 0.
    return [x for x in datos if x > 0]


# Creamos una función encargada de calcular estadísticas.
def calcular_estadisticas(datos):

    # Devolvemos un diccionario con tres resultados.
    return {

        # sum() suma todos los números.
        "suma": sum(datos),

        # Calculamos el promedio:
        # suma de los números / cantidad de números.
        "media": sum(datos) / len(datos),

        # max() obtiene el número más grande.
        "max": max(datos)
    }


# -------------------------
# PIPELINE MODULAR
# -------------------------

# Primero obtenemos los datos.
# En un programa real podrían provenir de un archivo CSV.
datos = leer_datos("archivo.csv")


# Después filtramos solamente los números positivos.
datos = filtrar_positivos(datos)


# Finalmente calculamos las estadísticas
# de los datos que quedaron.
estadisticas = calcular_estadisticas(datos)


# Mostramos los resultados.
print(estadisticas)
