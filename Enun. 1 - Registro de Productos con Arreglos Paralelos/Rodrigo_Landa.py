# Creamos tres listas paralelas.
# Los datos de un producto están en la misma posición en cada lista.
nombres = ["Laptop", "Mouse", "Teclado", "Monitor"]
precios = [2500, 60, 150, 700]
cantidades = [2, 10, 8, 5]

# Aquí acumularemos el valor de todo el inventario.
total_inventario = 0

# Recorremos los índices de las listas.
for i in range(len(nombres)):
    # Mostramos nombre, precio y stock del producto actual.
    # :.2f muestra el precio con dos decimales, dandonos a entender que es un valor monetario.
    print(f"{nombres[i]} | Precio: S/ {precios[i]:.2f} | Stock: {cantidades[i]}")

    # Calculamos el valor del stock de este producto.
    subtotal = precios[i] * cantidades[i]

    # Agregamos el subtotal al valor total del inventario.
    total_inventario += subtotal

# Mostramos el total después de recorrer todos los productos.
print(f"\nValor total del inventario: S/ {total_inventario:.2f}")
