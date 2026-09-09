#LAS FUNCIONES
def es_par(numero):
    return numero % 2 == 0

def mostrar_paridad(numero):
    #Verificamos si el número tiene decimales
    if numero != int(numero):
        print(f"El número {numero} no es entero. La paridad solo aplica a enteros")
    elif es_par(numero):
        print(f"El número {int(numero)} es PAR")
    else:
        print(f"El número {int(numero)} es IMPAR")

#EL PROGRAMA PRINCIPAL
num = float(input("Ingresa un número: "))

mostrar_paridad(num)
