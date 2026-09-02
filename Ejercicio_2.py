#Comparando dos números ingresados por el usuario, hayando el mayor, menor o si son iguales

N1 = float(input("Ingrese el primer número: "))

N2 = float(input("Ingrese el segundo número: "))

if N1 > N2:
    print("El primer número es mayor que el segundo número")

elif N1 == N2:
    print("Los dos números son iguales")

else:
    print("El segundo número es mayor que el primer número")