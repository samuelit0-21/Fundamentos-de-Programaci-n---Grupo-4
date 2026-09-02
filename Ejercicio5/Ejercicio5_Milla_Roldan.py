print("---Bienvenido---")
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = str(input("Ingrese el operador que quiera usar para sus dos números (+, -, *, /): "))

if operador == "+":
    resultado = num1 + num2
    print("La suma de sus dos números es: ",resultado)
elif operador == "-":
    resultado = num1 - num2
    print("La resta de sus dos números es: ",resultado)
elif operador == "*":
    resultado = num1*num2
    print("La multiplicación sus dos números es: ",resultado)
elif operador == "/":
    if num2 !=0:
        resultado = num1 / num2
        print("La división de sus dos números es: ",resultado)
    else:
        print("FATAL ERROR: no puede divir entre 0")
