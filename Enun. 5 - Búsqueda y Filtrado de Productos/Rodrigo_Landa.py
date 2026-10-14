# Lista de productos representados mediante diccionarios.
productos = [
    {"nombre": "Mouse inalámbrico", "categoria": "Accesorios", "precio": 80},
    {"nombre": "Teclado mecánico", "categoria": "Accesorios", "precio": 180},
    {"nombre": "Mouse gamer", "categoria": "Accesorios", "precio": 120},
    {"nombre": "Monitor", "categoria": "Pantallas", "precio": 650}
]


# La función recibe la lista de productos y el texto que se busca.
def buscar_productos(lista, termino):
    # Guardaremos aquí los productos que coincidan.
    resultados = []

    # Convertimos el término a minúsculas.
    termino = termino.lower()

    # Revisamos cada producto.
    for producto in lista:
        # in comprueba si el término aparece dentro del nombre.
        # lower() permite buscar sin importar mayúsculas.
        if termino in producto["nombre"].lower():
            # Agregamos el producto encontrado.
            resultados.append(producto)

    # Ordenamos los resultados por precio de menor a mayor.
    resultados.sort(key=lambda producto: producto["precio"])

    # Devolvemos la lista de productos encontrados.
    return resultados


# Llamamos a la función y guardamos su resultado.
resultados = buscar_productos(productos, "MOUSE")

print("Productos encontrados:")

# Mostramos los productos encontrados en orden de precio.
for producto in resultados:
    print(f"{producto['nombre']} | S/ {producto['precio']:.2f}")
