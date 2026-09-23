#Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
#Escribir un programa que calcule: promedio, nota más alta, nota más baja y cuántos aprobaron (nota ≥ 11)

Notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

print("1- Nos piden el promedio de la lista (notas)")

suma = sum(Notas)
cantidad = len(Notas)

Promedio = suma/cantidad

print(f"El promedio de la lista (notas) seria: {Promedio}")

print("2- Nos piden calcular la nota mas alta de la lista")
print(f"La nota mas alta de la lista es: {max(Notas)}")
  
print("3- Nos piden calcular la nota mas baja de la lista")
print(f"La nota mas baja de la lista es: {min(Notas)}")

print("4- Nos piden la cantidad de aprobados de la lista")

#Creamos el contador de aprobados con un for in range, mayor que 11 de nota se considera aprobado y va para el contador

Contador = 0

for i in range(len(Notas)):
    if Notas[i] >= 11:
        Contador += 1

print(f"La cantidad de aprobados en la lista son: {Contador}")
