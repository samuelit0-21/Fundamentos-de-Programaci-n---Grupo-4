historial = []

def visitar(url):
    historial.append(url)
    print(f"Visitaste: {url}")
    print("Pila actual:", historial)

def retroceder():
    if len(historial) > 0:
        pagina_eliminada = historial.pop()
        pagina_destino = historial[-1] if len(historial) > 0 else "Ninguna"
        print(f"Regresaste a: {pagina_destino}")

def pagina_actual():
    if len(historial) > 0:
        print("Página actual:", historial[-1])

#Historial
visitar("Google")
visitar("YouTube")
visitar("GitHub")

retroceder()
retroceder()

pagina_actual()
