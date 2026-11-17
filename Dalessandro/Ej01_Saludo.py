# Se define una función en la que debemos saludar a una persona
# Recibe dos parámetros: nombre y saludo.
def saludar(nombre, saludo="Hola"):
    # El formato es: <saludo>, <nombre>!
    print(f"{saludo}, {nombre}!") 

# Llamada usando el valor por defecto del parámetro saludo
saludar("Ana")

# Llamada especificando un saludo personalizado
saludar("Carlos", "Buenos días")
