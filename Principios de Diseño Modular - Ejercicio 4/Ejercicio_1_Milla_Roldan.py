# matematicas.py ← módulo independiente
def sumar(a, b): return a + b
def restar(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b):
    if b == 0: raise ValueError("División por cero")
    return a / b
# main.py
from matematicas import sumar, dividir
print(sumar(10, 5)) # 15
print(dividir(20, 4)) # 5.0
