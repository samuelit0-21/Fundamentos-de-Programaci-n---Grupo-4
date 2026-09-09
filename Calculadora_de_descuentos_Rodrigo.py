# Ejercicio 1 : Calculadora de Descuento

# Escribe una función llamada calcular_descuento(precio, porcentaje) que reciba el precio original de

# un producto y el porcentaje de descuento, y retorne el precio final después del descuento. Luego

# muestra el ahorro obtenido.

def calcular_descuento(precio, porcentaje):
  
    descuento = precio * (porcentaje / 100)
  
    precio_final = precio - descuento     
  
    return precio_final, descuento

# Hacemos la parte del pedido

precio_prod = float(input("Ingrese el precio del producto: "))

porcentaje_desc = float(input("Ingrese el porcentaje de descuento: "))

#Aplicamos la formula anterior

pago_final, ahorro = calcular_descuento(precio_prod, porcentaje_desc)

# Mostranos el resultado final:

print("El precio con descuento es:", pago_final)

print("El ahorro obtenido es:", ahorro)
