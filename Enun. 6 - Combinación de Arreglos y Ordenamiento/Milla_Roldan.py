# Listas paralelas: cada producto corresponde a las ventas de su posición.
productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
ventas = [10, 40, 25, 15]

# Esta lista almacenará los diccionarios.
registro = []

# Recorremos las posiciones de las listas.
for i in range(len(productos)):
    # Creamos un diccionario con el producto y sus ventas.
    registro.append({
        "nombre": productos[i],
        "ventas": ventas[i]
    })

# Ordenamos por ventas.
# reverse=True coloca primero los productos con más ventas.
registro.sort(key=lambda producto: producto["ventas"], reverse=True)

print("Ranking de ventas:")

# Recorremos la lista ya ordenada.
for i in range(len(registro)):
    # Obtenemos el producto de la posición actual.
    producto = registro[i]

    # Sumamos 1 al índice para que el ranking comience en 1°.
    print(f"{i + 1}° {producto['nombre']} | Ventas: {producto['ventas']}")

# Dividimos la suma de ventas entre la cantidad de productos.
promedio = sum(ventas) / len(ventas)

print(f"\nPromedio de ventas: {promedio:.2f}")
print("Productos sobre la media:")

# Revisamos cuáles superan el promedio.
for producto in registro:
    if producto["ventas"] > promedio:
        print(f"{producto['nombre']} | Ventas: {producto['ventas']}")
