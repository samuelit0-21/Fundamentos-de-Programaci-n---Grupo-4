class Empleado:
def __init__(self, nombre, salario):
self.nombre = nombre
self.__salario = salario
def aumentar_salario(self, pct):
self.__salario *= (1 + pct /
100)
@property
def salario(self):
return round(self.__salario, 2)
e = Empleado("Carlos", 3000)
e.aumentar_salario(10)
print(e.salario) # 3300.0
