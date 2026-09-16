# Ejercicio 3 — Inventario global
# Creamos una lista vacía llamada "inventario".
# Como está fuera de las funciones, es una variable GLOBAL.
inventario = []


# Creamos una función que recibe un producto.
def agregar(producto):

    # Indicamos que "inventario" hace referencia
    # a la variable global creada anteriormente.
    global inventario

    # append() agrega el producto recibido
    # al final de la lista.
    inventario.append(producto)


# Creamos una función para mostrar los productos.
def mostrar():

    # Recorremos todos los productos almacenados
    # dentro de la lista global "inventario".
    for p in inventario:

        # Mostramos cada producto.
        print(f" - {p}")


# Agregamos "Laptop" al inventario.
agregar("Laptop")

# Agregamos "Mouse" al inventario.
agregar("Mouse")

# Mostramos todos los productos guardados.
mostrar()

# Resultado:
# - Laptop
# - Mouse
