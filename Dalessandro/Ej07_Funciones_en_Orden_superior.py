# 1. map(): Convertir Celsius a Fahrenheit 
celsius = [0, 10, 20, 30, 40]

# map() aplica la función lambda a cada elemento de la lista
# La fórmula es: F = C * 9/5 + 32
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
print()


# 2. filter(): Obtener solo números pares 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter() mantiene solo los elementos que cumplen la condición
pares = list(filter(lambda x: x % 2 == 0, numeros))

print("Números originales:", numeros)
print("Solo pares:", pares)
print()


# 3. sorted() con lambda: Ordenar diccionarios por campo 
estudiantes = [
    {"nombre": "Ana", "nota": 15},
    {"nombre": "Carlos", "nota": 18},
    {"nombre": "Lucía", "nota": 12},
    {"nombre": "Pedro", "nota": 16}
]

# sorted() ordena la lista de diccionarios según el campo "nota" (de mayor a menor)
ordenados = sorted(estudiantes, key=lambda x: x["nota"], reverse=True)

print("Estudiantes ordenados por nota (mayor a menor):")
for est in ordenados:          # Solo para mostrar resultados (no es parte de la lógica principal)
    print(f"{est['nombre']}: {est['nota']}")
