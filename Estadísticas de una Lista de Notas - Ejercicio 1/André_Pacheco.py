#Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
#Escribir un programa que calcule: promedio, nota más alta, nota más baja y cuántos aprobaron (nota ≥ 11)


notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

print("1º- Nos piden el promedio de la lista (notas)")

sumando = sum(notas)
cantidad = len(notas)

promedio = sumando/cantidad

print(f"El promedio de la lista (notas) seria: {promedio}")
        

print("2º- Nos piden calcular la nota mas alta de la lista")
print(f"La nota mas alta de la lista es: {max(notas)}")

  
print("3º- Nos piden calcular la nota mas baja de la lista")
print(f"La nota mas baja de la lista es: {min(notas)}")


print("4º- Nos piden la cantidad de aprobados de la lista")

contador = 0
for i in range(len(notas)):
    if notas[i] >= 11:
        contador += 1
print(f"La cantidad de aprobados en la lista son: {contador}")
