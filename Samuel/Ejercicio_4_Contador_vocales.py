# Definimos una función que recibe un texto
def contar_vocales(texto):

    # Guardamos las vocales, incluyendo las que tienen tilde
    vocales = "aeiouáéíóú"

    # Inicializamos el contador en cero
    contador = 0

    # Convertimos el texto a minúsculas y recorremos cada letra
    for letra in texto.lower():

        # Verificamos si la letra pertenece a las vocales
        if letra in vocales:

            # Aumentamos el contador en uno
            contador += 1

    # Devolvemos la cantidad total de vocales
    return contador


# Guardamos un texto de ejemplo
texto = "Hola Vania, ¿cómo estás?"

# Mostramos la cantidad de vocales encontradas
print("Cantidad de vocales:", contar_vocales(texto))
