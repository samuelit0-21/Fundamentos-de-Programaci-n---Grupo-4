import re

catalogo = [
    {"titulo": "Aprende Python Fácil", "autor": "Guido Van", "año": 2020},
    {"titulo": "Estructuras de Datos", "autor": "Python Fan", "año": 2018},
    {"titulo": "Programación Básica", "autor": "Carlos Pérez", "año": 2021},
    {"titulo": "Python Avanzado", "autor": "Ana Gómez", "año": 2019}
]

def buscador(catalogo, query):
    resultados = []
    regex = re.compile(re.escape(query), re.IGNORECASE)
    
    for libro in catalogo:
        puntaje = 0
        if regex.search(libro["titulo"]):
            puntaje += 2  # Título vale 2 puntos
        if regex.search(libro["autor"]):
            puntaje += 1  # Autor vale 1 punto
            
        if puntaje > 0:
            libro_resultado = libro.copy()
            libro_resultado["puntaje"] = puntaje
            resultados.append(libro_resultado)
            
    resultados.sort(key=lambda x: (x["puntaje"], x["año"]), reverse=True)
    return resultados

print("=== BÚSQUEDA DE 'Python' ===")
for item in buscador(catalogo, "Python"):
    print(f"Título: {item['titulo']:<25} | Autor: {item['autor']:<12} | Año: {item['año']} | Puntaje: {item['puntaje']}")
