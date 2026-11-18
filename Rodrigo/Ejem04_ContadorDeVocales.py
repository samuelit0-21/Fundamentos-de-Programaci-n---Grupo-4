# Creamos una funcion para contar las vocales
def contar_vocales(texto):

    vocales = "aeiouáéíóú"
    contador = 0

    # Convertimos el texto a minusculas
    texto = texto.lower()

    # Recorremos cada letra del texto
    for letra in texto:

        # Verificamos si es una vocal
        if letra in vocales:
            contador += 1
          
    # Devolvemos la cantidad total de vocales
    return contador


# Programa principal
texto = input("Ingrese un texto: ")

resultado = contar_vocales(texto)

print("Cantidad de vocales:", resultado)
