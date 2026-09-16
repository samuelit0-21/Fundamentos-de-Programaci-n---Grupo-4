# Creamos una clase llamada Temperatura.
class Temperatura:

    # Constructor de la clase.
    # Recibe una temperatura en grados Celsius.
    def __init__(self, celsius):

        # Guardamos la temperatura en un atributo privado.
        self._celsius = celsius


    # @property permite utilizar un método
    # como si fuera un atributo normal.
    @property
    def celsius(self):

        # Retornamos el valor almacenado.
        return self._celsius


    # @celsius.setter permite controlar qué ocurre
    # cuando intentamos cambiar el valor de celsius.
    @celsius.setter
    def celsius(self, valor):

        # Comprobamos que la temperatura no sea
        # menor que el cero absoluto (-273.15 °C).
        if valor < -273.15:

            # Si el valor no es válido,
            # generamos un error.
            raise ValueError("Bajo cero absoluto")

        # Si el valor es válido,
        # actualizamos la temperatura.
        self._celsius = valor


# Creamos un objeto de la clase Temperatura.
t = Temperatura(0)

# Cambiamos la temperatura utilizando la propiedad.
# Aunque parece una asignación normal, Python ejecuta
# internamente el setter de celsius.
t.celsius = 25

# Consultamos la temperatura.
# Python ejecuta el método definido con @property.
print(t.celsius)  # 25
