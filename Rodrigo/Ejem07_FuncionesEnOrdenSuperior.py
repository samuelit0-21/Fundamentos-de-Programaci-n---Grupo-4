# Creamos una lista de temperaturas en Celsius
temperaturas = [0, 10, 20, 30, 40]

# Convertimos Celsius a Fahrenheit usando map()
fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperaturas))

print("Temperaturas en Fahrenheit:", fahrenheit)


# Creamos una lista de numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtramos los numeros pares usando filter()
pares = list(filter(lambda n: n % 2 == 0, numeros))

print("Numeros pares:", pares)


# Creamos una lista de estudiantes
estudiantes = [
    {"nombre": "Carlos", "nota": 15},
    {"nombre": "Maria", "nota": 18},
    {"nombre": "Pedro", "nota": 12}
]

# Ordenamos los estudiantes por nota usando sorted()
ordenados = sorted(estudiantes, key=lambda x: x["nota"])

print("Estudiantes ordenados:", ordenados)
