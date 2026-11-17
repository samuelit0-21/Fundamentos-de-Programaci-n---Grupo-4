# Importamos el módulo math para utilizar el valor de PI
import math

# Definimos una función para calcular el área de un círculo
def area_circulo(radio):

    # Aplicamos la fórmula: PI por radio al cuadrado
    return math.pi * radio ** 2


# Definimos una función para calcular el perímetro
def perimetro_circulo(radio):

    # Aplicamos la fórmula: 2 por PI por radio
    return 2 * math.pi * radio
