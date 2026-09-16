#Ejercicio-1

# Creamos una función llamada contar_vocales.
# El parámetro "texto" recibe la palabra o frase que queremos analizar.

def contar_vocales(texto):
  
  # Guardamos todas las vocales que queremos buscar.
  # Esta variable es LOCAL porque existe solamente dentro de la función.
  
  vocales = "aeiouAEIOU"
  
    # Creamos un contador que comienza en 0.
    # Aquí iremos acumulando la cantidad de vocales encontradas.
  
    conteo = 0

    # Recorremos el texto letra por letra.

    for letra in texto:

        # Comprobamos si la letra actual está dentro de la cadena "vocales".
      
        if letra in vocales:

            # Si encontramos una vocal, aumentamos el contador en 1.
          
            conteo += 1

    # Al terminar de recorrer el texto, devolvemos la cantidad de vocales.

    return conteo


# Llamamos a la función enviándole el texto "Hola Mundo".
# print() muestra en pantalla el resultado devuelto por la función.
print(contar_vocales("Hola Mundo"))  # Resultado: 4
