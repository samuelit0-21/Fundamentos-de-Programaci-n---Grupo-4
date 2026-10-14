# Importamos el módulo de expresiones regulares.
import re

# Catálogo de libros.
catalogo = [
    {"titulo": "Aprende Python", "autor": "Ana Torres", "año": 2022},
    {"titulo": "Python avanzado", "autor": "Luis Pérez", "año": 2024},
    {"titulo": "Programación básica", "autor": "Carlos Python", "año": 2021},
    {"titulo": "Python práctico", "autor": "María Python", "año": 2023},
    {"titulo": "Introducción a Java", "autor": "Elena Ruiz", "año": 2020}
]


# Recibe el catálogo y el texto que se desea buscar.
def buscador(catalogo, query):
    resultados = []

    # Si la búsqueda está vacía o solo tiene espacios, devolvemos una lista vacía.
    if not query.strip():
        return resultados

    # escape() permite buscar los símbolos del texto de forma literal.
    # IGNORECASE permite ignorar diferencias entre mayúsculas y minúsculas.
    patron = re.compile(re.escape(query), re.IGNORECASE)

    for libro in catalogo:
        # Cada libro comienza con cero puntos.
        puntaje = 0

        # Una coincidencia en el título suma 2 puntos.
        if patron.search(libro["titulo"]):
            puntaje += 2

        # Una coincidencia en el autor suma 1 punto.
        if patron.search(libro["autor"]):
            puntaje += 1

        # Solo guardamos los libros que tuvieron alguna coincidencia.
        if puntaje > 0:
            # Creamos una copia para no modificar el diccionario original.
            resultado = libro.copy()

            # Añadimos el puntaje a la copia.
            resultado["puntaje"] = puntaje

            resultados.append(resultado)

    # Ordenamos usando dos criterios:
    # 1. Puntaje de mayor a menor, gracias al signo negativo.
    # 2. Año de menor a mayor cuando los puntajes son iguales.
    resultados.sort(key=lambda libro: (-libro["puntaje"], libro["año"]))

    return resultados


# Buscamos la palabra Python en los títulos y autores.
resultados = buscador(catalogo, "python")

# Mostramos los resultados con su puntaje.
for libro in resultados:
    print(
        f"{libro['titulo']} | Autor: {libro['autor']} | "
        f"Año: {libro['año']} | Puntaje: {libro['puntaje']}"
    )
