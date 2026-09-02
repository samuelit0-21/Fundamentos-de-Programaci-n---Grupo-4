#Notas de estudiantes, vemos la nota más alta, la más baja y el promedio de las notas

n = int(input("Ingrese la cantidad de notas: "))

suma = 0
maxima = 0
minima = 20
aprobados = 0

for i in range(n):

    #Conteo de notas
    nota = int(input(f"Ingrese la nota {i + 1}: "))

    #Acumulacion para el paso del promedio
    suma = suma + nota

    #Conteo de aprobados
    if nota >= 11:
        aprobados = aprobados + 1

    #Nota mas alta y mas baja
    if i == 0:
       maxima = nota
       minima = nota
    elif nota > maxima:
       maxima = nota
    elif nota < minima:
       minima = nota

#Procedimiento del promedio
promedio = suma / n

####
print("EVALUACIÓN TERMINADA")
print("Promedio:", promedio)
print("Nota mas alta:", maxima)
print("Nota mas baja:", minima)
print("aprobados:", aprobados)
print("Desaprobados:", n - aprobados)
