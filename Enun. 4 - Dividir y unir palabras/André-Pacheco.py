cadena_colores = "rojo, verde, azul, amarillo"

#Separando por coma, espacios y convirtiendo a mayuscula
lista_colores = [color.strip().upper() for color in cadena_colores.split(",")]

#Uniendo con el separador ' | '
resultado = " | ".join(lista_colores)

print("Resultado:", resultado) 
