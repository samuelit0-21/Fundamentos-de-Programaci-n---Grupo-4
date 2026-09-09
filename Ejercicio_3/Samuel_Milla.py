#Ejercicio 3: Calculadora de Promedio con Lista

#    Escribe una función calcular_promedio(notas) que reciba una lista de notas y retorne el promedio, la nota
#    mínima y la nota máxima. Además crea una función mostrar_resultado(nombre, notas) sin retorno que muestre
#    un reporte formateado.


def calcular_promedio(notas):
    return sum(notas) / len(notas), min(notas), max(notas)

def mostrar_resultado(nombre, notas):
    prom, mn, mx = calcular_promedio(notas)
    print(f"\nEstudiante: {nombre} | Promedio: {prom:.2f} | Mín: {mn} | Máx: {mx}")

# EL PROGRAMA PRINCIPAL

# Pidiendo nombre al estudiante
nombre_alumno = input("Ingrese el nombre del estudiante: ")

# Pidiendo la cantidad de notas
cantidad = 0
while cantidad <= 0:
    try:
        cantidad = int(input("¿Cuántas notas desea ingresar?: "))
        if cantidad <= 0:
            print("Error: Ingrese un número mayor a 0")
    except ValueError:
        print("Error: Debe ingresar un número entero (sin decimales)")

# Procesando notas
notas_alumno = [0.0] * cantidad

for i in range(cantidad):
    nota = float(input(f"Nota {i+1}: "))
    while nota < 0 or nota > 20:
        print("Error: La nota debe estar entre 0 y 20")
        nota = float(input(f"Ingrese nuevamente la nota {i+1}: "))
    
    notas_alumno[i] = nota


# Mostrando el resultado final
mostrar_resultado(nombre_alumno, notas_alumno)
