#Ejercicio 3 - Celsius a Fahrenheit
# Creamos una función llamada celsius_a_fahrenheit.
# El parámetro "c" representa la temperatura en grados Celsius.
def celsius_a_fahrenheit(c):

    # Guardamos el factor de conversión 9/5.
    # "factor" es una variable LOCAL.
    factor = 9 / 5

    # Aplicamos la fórmula para convertir Celsius a Fahrenheit:
    # Fahrenheit = Celsius × 9/5 + 32
    # "fahrenheit" también es una variable LOCAL.
    fahrenheit = c * factor + 32

    # Devolvemos el resultado de la conversión.
    return fahrenheit


# Convertimos 100 grados Celsius a Fahrenheit.
print(celsius_a_fahrenheit(100))  # Resultado: 212.0

# Convertimos 0 grados Celsius a Fahrenheit.
print(celsius_a_fahrenheit(0))    # Resultado: 32.0
