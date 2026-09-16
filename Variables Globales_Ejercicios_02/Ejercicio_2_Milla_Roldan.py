# Creamos una variable global llamada MODO_DEBUG.
# True significa que el modo de depuración está activado.
MODO_DEBUG = True


# Creamos una función que recibe un dato.
def procesar(dato):

    # Consultamos el valor de la variable global MODO_DEBUG.
    # Como solamente estamos LEYENDO la variable y no modificándola,
    # no necesitamos escribir "global MODO_DEBUG".
    if MODO_DEBUG:

        # Si MODO_DEBUG es True, mostramos información
        # sobre el dato que se está procesando.
        print(f"[DEBUG] Procesando: {dato}")

    # upper() convierte el texto recibido a mayúsculas.
    # return devuelve el resultado.
    return dato.upper()


# Llamamos a la función enviando el texto "hola".
procesar("hola")   # [DEBUG] Procesando: hola
