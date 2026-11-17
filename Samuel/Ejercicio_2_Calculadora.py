# Definimos una función que recibe dos números y un operador
def calcular(a, b, operador):

    # Verificamos si el operador es una suma
    if operador == "+":
        return a + b

    # Verificamos si el operador es una resta
    elif operador == "-":
        return a - b

    # Verificamos si el operador es una multiplicación
    elif operador == "*":
        return a * b

    # Verificamos si el operador es una división
    elif operador == "/":

        # Comprobamos que el segundo número no sea cero
        if b == 0:
            print("Error: no se puede dividir entre cero")
            return None

        # Realizamos la división
        return a / b

    # Si el operador no es válido, mostramos un mensaje
    else:
        print("Error: operador no válido")
        return None


# Probamos la calculadora con diferentes operaciones
print(calcular(10, 5, "+"))
print(calcular(10, 5, "-"))
print(calcular(10, 5, "*"))
print(calcular(10, 5, "/"))

# Probamos la división entre cero
print(calcular(10, 0, "/"))
