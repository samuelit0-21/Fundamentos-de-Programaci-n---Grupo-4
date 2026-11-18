# Creamos una funcion para clasificar la temperatura
def clasificar_temperatura(temp):

    # Evaluamos los rangos de temperatura
    if temp < 10:
        return "Frio"

    elif temp < 20:
        return "Fresco"

    elif temp < 30:
        return "Calido"

    else:
        return "Caliente"


# Comprobamos que el programa principal funcione
temperatura = 25

resultado = clasificar_temperatura(temperatura)

print("Temperatura:", resultado)
