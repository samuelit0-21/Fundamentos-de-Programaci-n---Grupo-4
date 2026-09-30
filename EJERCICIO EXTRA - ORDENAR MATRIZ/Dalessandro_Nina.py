# Creamos la matriz con tres filas y tres columnas
matriz = [
    [1, 3, 4],
    [5, 8, 9],
    [2, 6, 7]
]

# Creamos una lista vacía para guardar todos los números
numeros = []

# Recorremos las filas mediante el índice i
for i in range(len(matriz)):

    # Recorremos las columnas de cada fila mediante el índice j
    for j in range(len(matriz[i])):

        # Agregamos cada número de la matriz a la lista
        numeros.append(matriz[i][j])

# Ordenamos la lista usando el método burbuja
# Cada pasada coloca el mayor número pendiente al final
for i in range(len(numeros) - 1):

    # No volvemos a comparar los números que ya quedaron ordenados
    for j in range(len(numeros) - 1 - i):

        # Comparamos un número con el que está a su derecha
        if numeros[j] > numeros[j + 1]:

            # Si están en el orden incorrecto, intercambiamos sus posiciones
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Empezamos en el índice 0 de la lista ordenada
posicion = 0

# Recorremos nuevamente las filas de la matriz
for i in range(len(matriz)):

    # Recorremos las columnas de cada fila
    for j in range(len(matriz[i])):

        # Colocamos el número correspondiente en la matriz
        matriz[i][j] = numeros[posicion]

        # Avanzamos al siguiente número de la lista
        posicion += 1

# Mostramos el título del resultado
print("Matriz ordenada:")

# Mostramos cada fila en una línea diferente
for fila in matriz:
    print(fila)
