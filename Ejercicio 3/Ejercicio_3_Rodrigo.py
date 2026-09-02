#Tabla de multiplicar de un numero ingresado por el usuario

Numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):

    Resultado = Numero * i
    
    print(f"{Numero} x {i} = {Resultado}")  
