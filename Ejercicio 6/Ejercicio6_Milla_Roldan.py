# EJERCICIO 6 - Números Primos hasta N
import math

# Solicitar el número N
n = int(input("Ingrese un número N: "))

print(f"Números primos desde 2 hasta {n}:")

# Recorrer los números desde 2 hasta N
for numero in range(2, n + 1):
    es_primo = True
    # Verificar divisibilidad desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False
            break
    # Si es primo, mostrarlo
    if es_primo:
        print(numero)
