#Ejercicio Extra - Variables locales independientes
# Creamos la primera función.
def funcion_a():

    # Creamos una variable LOCAL llamada "valor".
    # Esta variable solamente existe dentro de funcion_a().
    valor = 100

    # Devolvemos el contenido de "valor".
    return valor


# Creamos una segunda función diferente.
def funcion_b():

    # También podemos crear una variable llamada "valor".
    # Esta es OTRA variable local y es independiente
    # de la variable "valor" de funcion_a().
    valor = 200

    # Devolvemos el contenido de esta variable.
    return valor


# Ejecutamos ambas funciones.
# funcion_a() devuelve 100.
# funcion_b() devuelve 200.
# print() muestra ambos resultados.
print(funcion_a(), funcion_b())  # Resultado: 100 200
