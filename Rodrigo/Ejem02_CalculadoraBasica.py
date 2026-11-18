# Definimos la función para realizar operaciones matemáticas básicas
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
        if b != 0:
            return a / b
        else:
            return "Error: no se puede dividir entre cero"

    # Verificamos si el operador es un módulo
    elif operador == "%":
        if b != 0:
            return a % b
        else:
            return "Error: no se puede calcular el módulo entre cero"

    else:
        return "Operador no valido"


# Programa principal
print(calcular(10, 5, "+"))
print(calcular(10, 5, "+"))   
print(calcular(10, 5, "-"))   
print(calcular(10, 5, "*"))   
print(calcular(10, 5, "/"))   
print(calcular(10, 0, "/"))   
print(calcular(10, 5, "%"))   
