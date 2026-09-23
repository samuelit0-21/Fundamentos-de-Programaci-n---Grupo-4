#Enunciado:
#Dada la matriz 3×3: [[1,2,3],[4,5,6],[7,8,9]] — Calcular y mostrar la suma de cada fila y la suma de cada columna

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Suma de las filas:")

for i in range(len(matriz)):
    suma_fila = sum(matriz[i])
    print("Fila", i + 1, ":", suma_fila)


print("Suma de las columnas:")

for j in range(len(matriz[0])):
    suma_columna = 0

    for i in range(len(matriz)):
        suma_columna += matriz[i][j]

    print("Columna", j + 1, ":", suma_columna)
