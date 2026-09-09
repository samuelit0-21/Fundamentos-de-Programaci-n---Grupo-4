# Ejercicio 2: Verificados de Número Par o Impar

#  Crea una función es_par(numero) que retorne True si el número es par o False si es impar. Luego crea otra

#  función mostrar_paridad(numero) (sin return) que use la primera función e imprima el resultado en pantalla

#  con un mensaje.

#Imprimimos las funciones
def es_par(numero):
  
    return numero % 2 == 0

def mostrar_paridad(numero):
  
    #Verificamos si el número tiene decimales
  
    if numero != int(numero):
        print(f"El número {numero} no es entero. La paridad solo aplica a enteros.")
      
    elif es_par(numero):
        print(f"El número {int(numero)} es PAR")
      
    else:
        print(f"El número {int(numero)} es IMPAR")

#Hacemos el programa principal
num = float(input("Ingresa un número: "))

mostrar_paridad(num)
