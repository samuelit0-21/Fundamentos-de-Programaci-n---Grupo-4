class Producto:
    
    # Clase que representa un producto con nombre, precio y stock.
    # Permite aplicar descuentos y vender unidades controlando el stock disponible.
    
    def __init__(self, nombre, precio, stock):
        # Inicializa los atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def aplicar_descuento(self, porcentaje):
        
        # Aplica un descuento al precio del producto.
        # El porcentaje debe ser un valor entre 0 y 100.
        
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
        
        # Calcula el nuevo precio aplicando el descuento
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
    
    def vender(self, cant):
        
        # Reduce el stock del producto según la cantidad vendida.
        # Lanza ValueError si no hay suficiente stock.
        
        if cant <= 0:
            raise ValueError("La cantidad a vender debe ser mayor que cero.")
        
        if cant > self.stock:
            raise ValueError(f"No hay suficiente stock. Stock disponible: {self.stock}")
        
        # Descuenta la cantidad vendida del stock
        self.stock -= cant
    
    def __str__(self):
        
        # Retorna una representación en cadena del producto.
        # Se utiliza automáticamente al hacer print(producto).
        
        return f"Producto: {self.nombre} | Precio: {self.precio:.2f} | Stock: {self.stock}"


# Ejemplos de uso
producto = Producto("Laptop", 1200.0, 10)
print(producto)

producto.aplicar_descuento(10)   # Aplica 10% de descuento
print(producto)

producto.vender(3)               # Vende 3 unidades
print(producto)

# Intento de vender más de lo disponible (generará error)
# producto.vender(10)
