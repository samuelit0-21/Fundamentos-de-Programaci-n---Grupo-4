# Creamos una función que recibe una temperatura
def clasificar_temperatura(temp):

    # Si la temperatura es menor a 10, es frío
    if temp < 10:
        return "Frío"

    # Si es menor a 20, es fresco
    elif temp < 20:
        return "Fresco"

    # Si es menor a 30, es cálido
    elif temp < 30:
        return "Cálido"

    # Si no cumple ninguna condición anterior, es caliente
    else:
        return "Caliente"


# Probamos la función con diferentes temperaturas
print(clasificar_temperatura(5))
print(clasificar_temperatura(15))
print(clasificar_temperatura(25))
print(clasificar_temperatura(35))
