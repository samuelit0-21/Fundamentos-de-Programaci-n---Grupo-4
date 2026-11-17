# Creamos la clase Producto
class Producto:

    # Método constructor que recibe los datos del producto
    def __init__(self, nombre, precio, stock):

        # Guardamos el nombre del producto
        self.nombre = nombre

        # Guardamos el precio del producto
        self.precio = precio

        # Guardamos la cantidad disponible
        self.stock = stock

    # Método para aplicar un descuento al precio
    def aplicar_descuento(self, porcentaje):

        # Validamos que el descuento esté entre 0 y 100
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("Descuento no válido")

        # Calculamos el nuevo precio con el descuento aplicado
        self.precio = self.precio * (1 - porcentaje / 100)

    # Método para vender una cantidad de productos
    def vender(self, cantidad):

        # Verificamos que la cantidad sea mayor a cero
        if cantidad <= 0:
            raise ValueError("Cantidad no válida")

        # Comprobamos que exista suficiente stock
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock")

        # Descontamos del stock las unidades vendidas
        self.stock -= cantidad

        # Calculamos y devolvemos el total de la venta
        return self.precio * cantidad

    # Método para mostrar los datos del producto
    def __str__(self):

        # Devolvemos el nombre, precio y stock
        return (
            f"Producto: {self.nombre}\n"
            f"Precio: S/ {self.precio:.2f}\n"
            f"Stock: {self.stock}"
        )


# Creamos un objeto de la clase Producto
producto = Producto("Laptop", 2500, 10)

# Aplicamos un descuento del 10% al producto
producto.aplicar_descuento(10)

# Mostramos los datos del producto actualizado
print(producto)

# Vendemos dos unidades del producto
total = producto.vender(2)

# Mostramos el importe total de la venta
print("\nTotal de venta: S/", total)

# Mostramos el stock que queda después de la venta
print("Stock restante:", producto.stock)
