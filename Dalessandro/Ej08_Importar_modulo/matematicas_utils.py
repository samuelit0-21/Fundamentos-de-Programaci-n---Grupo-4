# Importamos el módulo estándar 'math' para acceder al valor exacto de Pi (math.pi)
import math

def area_circulo(radio):
    """
    Función que calcula el área de un círculo.
    Fórmula: Área = pi * radio^2
    """
    return math.pi * (radio ** 2)

def perimetro_circulo(radio):
    """
    Función que calcula el perímetro (circunferencia) de un círculo.
    Fórmula: Perímetro = 2 * pi * radio
    """
    return 2 * math.pi * radio
