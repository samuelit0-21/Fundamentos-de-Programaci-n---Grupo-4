# Ejercicio 2 — Validación modular
# Creamos una función encargada únicamente
# de comprobar si un correo parece válido.
def validar_email(email):

    # Verificamos que el correo contenga "@"
    # y también un punto ".".
    return "@" in email and "." in email


# Creamos otra función encargada únicamente
# de comprobar la contraseña.
def validar_password(pwd):

    # len() obtiene la cantidad de caracteres.
    # Consideramos válida una contraseña
    # que tenga 8 o más caracteres.
    return len(pwd) >= 8


# Esta función combina las dos validaciones anteriores.
def validar_formulario(email, pwd):

    # Primero ejecutamos validar_email().
    # Después ejecutamos validar_password().
    # "and" exige que AMBAS condiciones sean True.
    return validar_email(email) and validar_password(pwd)


# Probamos nuestro formulario.
resultado = validar_formulario(
    "samuel@gmail.com",
    "python123"
)

# Mostramos el resultado.
print(resultado)  # True
