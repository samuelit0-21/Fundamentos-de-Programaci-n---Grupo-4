
n = int(input("Ingrese la cantidad de notas: "))

suma = 0
maxima = 0
minima = 20
aprobados = 0

for i in range(n):

    nota = int(input(f"Ingrese la nota {i + 1}: "))

    if nota > 20:
       print ("La nota no puede ser mayor a 20, Se Ajustará a 20.")
       nota = 20
    elif nota < 0:
       print("La nota no puede ser menor a 0. Se ajustará a 0.")
       nota = 0

    suma = suma + nota

    if nota >= 11:
        aprobados = aprobados + 1

    if i == 0:
       maxima = nota
       minima = nota
    elif nota > maxima:
       maxima = nota
    elif nota < minima:
       minima = nota

promedio = suma / n

print("EVALUACIÓN TERMINADA")
print("Promedio:", promedio)
print("Nota mas alta:", maxima)
print("Nota mas baja:", minima)
print("aprobados:", aprobados)
print("Desaprobados:", n - aprobados)
