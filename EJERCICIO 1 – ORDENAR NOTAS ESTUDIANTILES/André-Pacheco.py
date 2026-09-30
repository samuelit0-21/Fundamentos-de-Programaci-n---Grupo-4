notas = [85, 42, 93, 67, 28, 75]

def ordenar_burbuja(lista):
    resultado = lista.copy()
    longitud = len(resultado)
    for i in range(longitud):
        for j in range(0, longitud - i - 1):
            if resultado[j] > resultado[j + 1]:
                resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
    return resultado

def ordenar_seleccion(lista):
    resultado = lista.copy()
    longitud = len(resultado)
    for i in range(longitud):
        posicion_minima = i
        for j in range(i + 1, longitud):
            if resultado[j] < resultado[posicion_minima]:
                posicion_minima = j
        resultado[i], resultado[posicion_minima] = resultado[posicion_minima], resultado[i]
    return resultado

print("a) Bubble Sort:", ordenar_burbuja(notas))
print("b) Selection Sort:", ordenar_seleccion(notas))
print("c) Nota Mínima:", min(notas))
print("   Nota Máxima:", max(notas))
print(f"   Promedio: {sum(notas)/len(notas):.2f}")
