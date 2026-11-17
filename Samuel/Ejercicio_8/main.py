# Importamos nuestro módulo propio utilizando el alias mu
import matematicas_utils as mu


# Creamos una función que recibe una lista de radios
def reporte_geometrico(radios):

    # Mostramos el título del reporte
    print("REPORTE GEOMÉTRICO")

    # Imprimimos una línea para separar el encabezado
    print("-" * 55)

    # Mostramos los nombres de las columnas
    print(f"{'Radio':<10} {'Área':<20} {'Perímetro':<20}")

    # Imprimimos otra línea divisoria
    print("-" * 55)

    # Recorremos cada radio de la lista
    for radio in radios:

        # Calculamos el área utilizando el módulo importado
        area = mu.area_circulo(radio)

        # Calculamos el perímetro utilizando el módulo importado
        perimetro = mu.perimetro_circulo(radio)

        # Mostramos los resultados en forma de tabla
        # :.2f permite mostrar solamente dos decimales
        print(f"{radio:<10} {area:<20.2f} {perimetro:<20.2f}")


# Creamos una lista con diferentes radios
radios = [2, 4, 6, 8]

# Llamamos a la función para generar el reporte
reporte_geometrico(radios)
