#Ejercicio 3: Calculadora de Promedio con Lista

#    Escribe una función calcular_promedio(notas) que reciba una lista de notas y retorne el promedio, la nota
#    mínima y la nota máxima. Además crea una función mostrar_resultado(nombre, notas) sin retorno que muestre
#    un reporte formateado.


def calcular_promedio(notas):
    return sum(notas) / len(notas), min(notas), max(notas)

def mostrar_resultado(nombre, notas):
    prom, mn, mx = calcular_promedio(notas)
    print(f"\nEstudiante: {nombre} | Promedio: {prom:.2f} | Mín: {mn} | Máx: {mx}")

