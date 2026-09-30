# Creamos una lista vacía para guardar los clientes que esperan
cola = []


def tomar_turno(cliente):
    # Agregamos al cliente al final de la cola
    cola.append(cliente)

    print("Tomó turno:", cliente)


def atender():
    # Verificamos si hay clientes esperando
    if cola:

        # Quitamos al primer cliente y guardamos su nombre
        # El índice 0 corresponde al inicio de la cola
        cliente = cola.pop(0)

        print("Cliente atendido:", cliente)

    else:
        # Si la cola está vacía, no podemos atender
        print("No hay clientes esperando.")


def mostrar_cola():
    # Mostramos la cantidad de clientes que esperan
    print("Clientes esperando:", len(cola))

    # Mostramos sus nombres en orden de llegada
    print("Cola actual:", cola)


# Llegan cuatro clientes al banco
tomar_turno("Ana")
tomar_turno("Luis")
tomar_turno("Pedro")
tomar_turno("Maria")

# Mostramos los cuatro clientes que esperan
mostrar_cola()

# Atendemos a los dos primeros clientes
atender()
atender()

# Mostramos los clientes que siguen esperando
mostrar_cola()

# Llega un cliente más y se coloca al final
tomar_turno("Carlos")

# Mostramos la cola antes de continuar atendiendo
mostrar_cola()

# Mientras haya clientes en la cola, seguimos atendiendo
while cola:
    atender()

# Mostramos que la cola quedó vacía
mostrar_cola()
