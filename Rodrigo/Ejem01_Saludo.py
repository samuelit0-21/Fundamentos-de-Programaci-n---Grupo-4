# Se define una función en la que debemos saludar a una persona
# Se reciben dos parámetros: nombre y saludo.
def saludar(nombre, saludo="Hola"):
  # Se muestra el saludo con el nombre 
    print(f"{saludo}, {nombre}!")

# Programa principal

# Llamada usando el valor por defecto del parámetro saludo
saludar("Carlos")

# Llamada especificando un saludo personalizado 
saludar("Carlos", "Buenos dias")
