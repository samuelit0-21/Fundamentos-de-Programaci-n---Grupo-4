# Definimos una función para saludar a una persona
# El parámetro saludo tiene "Hola" como valor predeterminado
def saludar(nombre, saludo="Hola"):

    # Mostramos el saludo junto con el nombre
    print(f"{saludo}, {nombre}!")


# Llamamos a la función utilizando el saludo predeterminado
saludar("Vania")

# Llamamos a la función indicando un saludo diferente
saludar("Karina", "Buenos días")
