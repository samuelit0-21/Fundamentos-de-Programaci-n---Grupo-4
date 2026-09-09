#LA FUNCIÓN
def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento        
    return precio_final, descuento

#EL PROGRAMA PRINCIPAL (El pedido)

#Le pides los datos a la persona
precio_prod = float(input("Ingrese el precio del producto: "))
porcentaje_desc = float(input("Ingrese el porcentaje de descuento: "))

#Usando la formula de arriba
pago_final, ahorro = calcular_descuento(precio_prod, porcentaje_desc)

#Muestras el resultado final:
print("El precio con descuento es:", pago_final)
print("El ahorro obtenido es:", ahorro)
