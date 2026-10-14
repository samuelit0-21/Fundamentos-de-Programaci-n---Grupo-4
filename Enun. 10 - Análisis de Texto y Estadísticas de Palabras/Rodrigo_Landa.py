# Importamos el módulo para usar expresiones regulares.
import re


# La función recibe el párrafo que se analizará.
def analizar_texto(texto):
    # [^\W\d_] captura letras, incluyendo letras con tilde.
    # Excluye números y guiones bajos.
    # La segunda parte permite apóstrofes dentro de las palabras.
    patron = r"[^\W\d_]+(?:['’][^\W\d_]+)*"

    # lower() convierte el texto a minúsculas.
    # findall() devuelve una lista con todas las palabras encontradas.
    palabras = re.findall(patron, texto.lower())

    # Guardaremos cada palabra junto con su cantidad de apariciones.
    frecuencias = {}

    for palabra in palabras:
        # get(palabra, 0) obtiene el contador actual.
        # Si la palabra todavía no existe, devuelve cero.
        # Después sumamos una aparición.
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    # items() devuelve pares de palabra y frecuencia.
    # elemento[0] es la palabra y elemento[1] es su frecuencia.
    # Ordenamos primero por frecuencia descendente.
    # Si hay empate, ordenamos alfabéticamente.
    ordenadas = sorted(
        frecuencias.items(),
        key=lambda elemento: (-elemento[1], elemento[0])
    )

    print("TOP 5 DE PALABRAS MÁS FRECUENTES")

    # [:5] selecciona los primeros cinco resultados.
    for palabra, frecuencia in ordenadas[:5]:
        print(f"{palabra}: {frecuencia}")

    # Las claves del diccionario ya son palabras sin repetir.
    # sorted() las coloca en orden alfabético.
    palabras_unicas = sorted(frecuencias)

    print("\nPALABRAS ÚNICAS ORDENADAS")
    print(palabras_unicas)

    # Devolvemos el diccionario por si necesitamos utilizarlo después.
    return frecuencias


# Párrafo de ejemplo.
parrafo = (
    "Python es un lenguaje de programación. "
    "Python es fácil de aprender y la programación es divertida. "
    "Aprender Python permite crear programas."
)

# Ejecutamos el análisis del párrafo.
analizar_texto(parrafo)
