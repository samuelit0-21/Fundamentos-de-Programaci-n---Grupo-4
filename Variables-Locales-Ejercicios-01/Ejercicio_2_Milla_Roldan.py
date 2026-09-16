#Ejercicio 2 - Calcular el promedio
# Creamos una función llamada promedio.
# El parámetro "numeros" recibirá una lista de números.

def promedio(numeros):

    # sum() suma todos los números de la lista.
    # "total" es una variable LOCAL de esta función.
    total = sum(numeros)

    # len() obtiene la cantidad de elementos que tiene la lista.
    # "n" también es una variable LOCAL.
    n = len(numeros)

    # Comprobamos si la lista contiene elementos.
    # Esto evita intentar dividir entre 0.
    if n:

        # Si hay elementos, dividimos la suma total
        # entre la cantidad de números.
        return total / n

    # Si la lista está vacía, devolvemos 0.
    else:
        return 0


# Enviamos una lista con los números 10, 20 y 30.
# La función realiza: (10 + 20 + 30) / 3
print(promedio([10, 20, 30]))  # Resultado: 20.0
