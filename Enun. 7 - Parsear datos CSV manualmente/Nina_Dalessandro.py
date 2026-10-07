texto = "Este es un texto con contenido secreto y privado."
prohibidas = ["secreto", "privado"]

for palabra in prohibidas:
    asteriscos = "*" * len(palabra)
    texto = texto.replace(palabra, asteriscos)

print("Texto censurado:", texto)
