matriz = [
    [1, 3, 4],
    [5, 8, 9],
    [2, 6, 7]
]

numeros = []

# Guardamos los elementos de la matriz en una lista
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        numeros.append(matriz[i][j])

# Ordenamos la lista mediante burbuja
for i in range(len(numeros) - 1):
    for j in range(len(numeros) - 1 - i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

# Colocamos los números ordenados en la matriz
posicion = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = numeros[posicion]
        posicion += 1

print("Matriz ordenada:")

for fila in matriz:
    print(fila)
