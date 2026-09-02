#Debemos adivinar un número que diga la computadora, el usuario tiene que adivinarlo, si no lo adivina sigue el juego, si acierta acaba

import random

Numero_secreto = random.randint(1, 100)

Intentos = 0

print ("Adivina el número secreto entre 1 y 100")

while True:
    Intento = int(input("Ingrese su intento: "))
    Intentos += 1

    if Intento < Numero_secreto:
        print("El número secreto es mayor.")

    elif Intento > Numero_secreto:
        print("El número secreto es menor.")

    else:
        print (f"¡Correcto lo adivinaste, el número secreto era {Numero_secreto}!") 
        print (f"Lo adivinaste en {Intentos} intento(s).")
        break
