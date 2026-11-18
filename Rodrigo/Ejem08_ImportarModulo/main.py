# Importamos nuestro modulo propio
import matematicas_utils as mu

# Solicitamos el radio al usuario
radio = float(input("Ingrese el radio del circulo: "))

# Calculamos el area
area = mu.area_circulo(radio)

# Calculamos el perimetro
perimetro = mu.perimetro_circulo(radio)

# Mostramos los resultados
print("Area del circulo:", area)

print("Perimetro del circulo:", perimetro)
