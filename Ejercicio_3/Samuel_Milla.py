#LA FUNCIÓN
def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento        
    return precio_final, descuento
