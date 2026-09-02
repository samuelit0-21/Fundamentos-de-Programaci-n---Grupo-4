import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("Adivine el número secreto (entre 1 y 100).")

while True:
    intento = int(input("Ingrese su intento: "))
    intentos += 1
    
    if intento < numero_secreto:
        print("El número secreto es mayor.")
    elif intento > numero_secreto:
        print("El número secreto es menor.")
    else:
        print(f"¡Correcto! El número era {numero_secreto}.")
        print(f"Lo adivinó en {intentos} intento(s).")
        break
