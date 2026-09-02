# EJERCICIO 7 - Adivina el Número (Do-While)
import random 

numero_secreto_secretito = random.randint(1,100)

intentos = 0

print("Adivine el número secreto (entre 1 y 100).")

while True:
    intento = int(input("Ingrese su intento: "))
    intentos += 1
    
    if intento < numero_secreto_secretito:
        print("El número secreto es mayor.")
    elif intento > numero_secreto_secretito:
        print("El número secreto es menor.")
    else:
        print(f"El número era {numero_secreto_secretito}.")
        print(f"Lo adivinó en {intentos} intento(s).")
        break
