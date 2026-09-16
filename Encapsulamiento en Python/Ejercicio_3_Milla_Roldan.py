# Creamos una clase llamada Empleado.
class Empleado:

    # El constructor recibe el nombre y salario
    # del nuevo empleado.
    def __init__(self, nombre, salario):

        # Guardamos el nombre del empleado.
        self.nombre = nombre

        # Guardamos el salario en un atributo privado.
        self.__salario = salario


    # Creamos una propiedad para poder consultar
    # el salario de forma controlada.
    @property
    def salario(self):

        # Retornamos el salario redondeado
        # a dos posiciones decimales.
        return round(self.__salario, 2)


    # Creamos un método para aumentar el salario.
    # "pct" representa el porcentaje de aumento.
    def aumentar_salario(self, pct):

        # Calculamos el nuevo salario.
        # Por ejemplo, si pct = 10:
        # salario * (1 + 10 / 100)
        self.__salario *= (1 + pct / 100)


# Creamos un empleado llamado Carlos
# con un salario inicial de 3000.
e = Empleado("Carlos", 3000)

# Aumentamos su salario en 10%.
e.aumentar_salario(10)

# Consultamos el nuevo salario.
print(e.salario)  # 3300.0
