#Ejercicio 1 - Contador global de visitas
# Creamos la variable "visitas" fuera de cualquier función.
# Por estar fuera de la función, es una variable GLOBAL.
visitas = 0


# Creamos una función que registrará cada nueva visita.
def registrar_visita():

    # Indicamos que queremos modificar la variable global "visitas".
    # Sin "global", Python consideraría "visitas" como una variable local
    # al intentar modificarla dentro de la función.
    global visitas

    # Aumentamos el valor de visitas en 1.
    visitas += 1

    # Mostramos el número actual de la visita.
    print(f"Visita #{visitas} registrada")


# Ejecutamos la función por primera vez.
# visitas pasa de 0 a 1.
registrar_visita()   # Visita #1 registrada

# Ejecutamos nuevamente la función.
# visitas pasa de 1 a 2.
registrar_visita()   # Visita #2 registrada

# Mostramos el valor final de la variable global.
print(f"Total: {visitas}")   # Total: 2
