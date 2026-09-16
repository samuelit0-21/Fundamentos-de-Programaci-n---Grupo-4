# Ejercicio 1 — Módulo de operaciones matemáticas
# matematicas.py
# Este archivo funciona como un módulo independiente.
# Aquí colocamos funciones matemáticas que después
# pueden ser utilizadas desde otros archivos.


# Creamos una función llamada sumar.
# Recibe dos valores: a y b.
def sumar(a, b):

    # Sumamos los dos valores y devolvemos el resultado.
    return a + b


# Creamos una función para realizar una resta.
def restar(a, b):

    # Restamos b a la variable a.
    return a - b


# Creamos una función para realizar una multiplicación.
def multiplicar(a, b):

    # Multiplicamos ambos valores.
    return a * b


# Creamos una función para realizar una división.
def dividir(a, b):

    # Comprobamos si el divisor "b" es igual a 0.
    if b == 0:

        # Si b es 0, generamos un error porque
        # matemáticamente no se puede dividir entre cero.
        raise ValueError("División por cero")

    # Si b no es 0, realizamos la división
    # y devolvemos el resultado.
    return a / b
