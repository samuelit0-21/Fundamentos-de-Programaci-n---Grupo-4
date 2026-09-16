# Ejercicio 3 — Interruptor ON/OFF
# Creamos la función principal que construirá
# nuestro interruptor.
def crear_interruptor():

    # False representa que inicialmente
    # el interruptor está apagado.
    estado = False

    # Creamos una función interna para cambiar el estado.
    def cambiar():

        # Indicamos que queremos modificar la variable "estado"
        # perteneciente a crear_interruptor().
        nonlocal estado

        # "not" invierte un valor booleano.
        # False se convierte en True.
        # True se convierte en False.
        estado = not estado

        # Si estado es True, devolvemos "ON".
        # Si estado es False, devolvemos "OFF".
        return "ON" if estado else "OFF"

    # Devolvemos la función interna cambiar().
    return cambiar


# Creamos el interruptor.
# "switch" contiene la función cambiar().
switch = crear_interruptor()

# Estado inicial: False
# Se cambia a True.
print(switch())  # ON

# Estado anterior: True
# Se cambia a False.
print(switch())  # OFF

# Estado anterior: False
# Se cambia nuevamente a True.
print(switch())  # ON
