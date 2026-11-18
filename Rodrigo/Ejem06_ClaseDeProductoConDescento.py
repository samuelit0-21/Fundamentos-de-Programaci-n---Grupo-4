# Creamos la clase Producto
class Producto:

    # Inicializamos los atributos
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    # Metodo para aplicar descuento
    def aplicar_descuento(self, porcentaje):
        self.precio = self.precio - (self.precio * porcentaje / 100)

    # Metodo para vender productos
    def vender(self, cantidad):

        # Verificamos si hay suficiente stock
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock")

        # Descontamos los productos vendidos
        self.stock = self.stock - cantidad

        print("Venta realizada correctamente")

    # Metodo para mostrar los datos
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Stock: {self.stock}"


# Programa principal
producto1 = Producto("Laptop", 2000, 10)

# Aplicamos un descuento del 10%
producto1.aplicar_descuento(10)

# Mostramos los datos del producto
print(producto1)

# Vendemos 2 productos
producto1.vender(2)

# Mostramos el stock actualizado
print(producto1)
