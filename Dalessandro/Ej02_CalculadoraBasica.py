def calcular(a, b, operador):
    
    # Función que realiza operaciones básicas (+, -, *, /) entre dos números.
    # Retorna el resultado de la operación o None si hay un error.
    
    # Validación del operador y realización de la operación correspondiente
    if operador == "+":
        # Suma
        return a + b
    elif operador == "-":
        # Resta
        return a - b
    elif operador == "*":
        # Multiplicación
        return a * b
    elif operador == "/":
        # División: se valida que el divisor no sea cero
        if b != 0:
            return a / b
        else:
            print("Error: división por cero no permitida.")
            return None
    else:
        # Operador no válido
        print("Error: operador no válido. Use +, -, * o /.")
        return None

# Pruebas de uso.
print(calcular(10, 5, "+"))   
print(calcular(10, 5, "-"))   
print(calcular(10, 5, "*"))   
print(calcular(10, 5, "/"))   
print(calcular(10, 0, "/"))   
print(calcular(10, 5, "%"))   
