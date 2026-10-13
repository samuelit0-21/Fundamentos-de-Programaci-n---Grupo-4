productos = [
    {"nombre": "Teclado Mecánico", "categoria": "Periféricos", "precio": 250.0},
    {"nombre": "Mouse Gamer", "categoria": "Periféricos", "precio": 120.0},
    {"nombre": "Teclado Membrana", "categoria": "Periféricos", "precio": 80.0},
    {"nombre": "Monitor 24", "categoria": "Pantallas", "precio": 550.0}
]

def buscar_productos(lista, termino):
    
    coincidencias = [p for p in lista if termino.lower() in p["nombre"].lower()]
    
    coincidencias.sort(key=lambda x: x["precio"])
    return coincidencias

resultado = buscar_productos(productos, "teclado")
print("=== PRODUCTOS ENCONTRADOS (ORDENADOS POR PRECIO) ===")
for prod in resultado:
    print(f"- {prod['nombre']} | Precio: S/.{prod['precio']}")
