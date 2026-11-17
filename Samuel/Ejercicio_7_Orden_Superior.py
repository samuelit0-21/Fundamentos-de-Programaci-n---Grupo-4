# 1. MAP: convertir temperaturas de Celsius a Fahrenheit

# Creamos una lista de temperaturas en Celsius
temperaturas = [0, 10, 20, 30, 40]

# Utilizamos map() para convertir cada temperatura
# La fórmula convierte grados Celsius a Fahrenheit
fahrenheit = list(
    map(lambda c: (c * 9/5) + 32, temperaturas)
)

# Mostramos las temperaturas convertidas
print("Temperaturas Fahrenheit:", fahrenheit)


# 2. FILTER: seleccionar solamente números pares

# Creamos una lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Utilizamos filter() para seleccionar números pares
# El operador % calcula el residuo de una división
pares = list(
    filter(lambda n: n % 2 == 0, numeros)
)

# Mostramos los números pares
print("Números pares:", pares)


# 3. SORTED: ordenar productos por precio

# Creamos una lista de diccionarios con productos y precios
productos = [
    {"nombre": "Laptop", "precio": 2500},
    {"nombre": "Mouse", "precio": 50},
    {"nombre": "Teclado", "precio": 120}
]

# Utilizamos sorted() para ordenar por el precio
# lambda indica que el criterio de ordenamiento es el precio
ordenados = sorted(
    productos,
    key=lambda producto: producto["precio"]
)

# Mostramos los productos ordenados de menor a mayor precio
print("Productos ordenados:", ordenados)
