def contar_vocales(texto):
    
    # Cuenta la cantidad de vocales (a, e, i, o, u, incluyendo tildes)
    # que contiene un texto, sin distinguir entre mayúsculas y minúsculas.
    
    # Convertir todo el texto a minúsculas para ignorar mayúsculas
    texto = texto.lower()
    
    # Cadena que contiene todas las vocales a considerar (con y sin tilde)
    vocales = "aeiouáéíóú"
    
    # Contador de vocales encontradas
    contador = 0
    
    # Recorrer cada carácter del texto
    for caracter in texto:
        # Verificar si el carácter actual es una vocal
        if caracter in vocales:
            contador += 1
    
    # Retornar el total de vocales encontradas
    return contador

# Ejemplos de uso (opcionales, para probar la función)
print(contar_vocales("Hola Mundo"))           # 4
print(contar_vocales("ÁÉÍÓÚáéíóú"))           # 10
print(contar_vocales("Python es genial"))     # 5
print(contar_vocales("BCDFG"))                # 0
print(contar_vocales("ABC"))                  # 1
