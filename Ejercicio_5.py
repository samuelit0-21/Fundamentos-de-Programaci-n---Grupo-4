#Calculadora simple que realiza operaciones básicas como suma, resta, multiplicación y división

N1 = float(input("Ingrese el primer número: ")) 

N2 = float(input("Ingrese el segundo número: "))

Operacion = input("Ingrese la operación que desea realizar (+, -, *, /): ")

if Operacion == "+":
    Resultado = N1 + N2
    print("El resultado de la suma es:", Resultado)

elif Operacion == "-":
    Resultado = N1 - N2
    print("El resultado de la resta es:", Resultado)

elif Operacion == "*":
    Resultado = N1 * N2
    print("El resultado de la multiplicación es:", Resultado)

elif Operacion == "/":
    if N2 != 0:
        Resultado = N1 / N2
        print("El resultado de la división es:", Resultado)
    else:
        print("Error: No se puede dividir entre cero.")