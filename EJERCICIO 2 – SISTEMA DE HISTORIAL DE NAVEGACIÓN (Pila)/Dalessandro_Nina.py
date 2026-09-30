# Creamos una pila vacía para guardar las páginas visitadas
historial = []


def visitar(url):
    # Agregamos la página al final de la pila
    historial.append(url)

    # Mostramos la página visitada y el historial completo
    print("Visitaste:", url)
    print("Pila actual:", historial)


def retroceder():
    # Necesitamos al menos dos páginas para regresar a la anterior
    if len(historial) > 1:

        # Quitamos la última página de la pila
        historial.pop()

        # Mostramos la página a la que regresamos
        # El índice -1 permite acceder al último elemento
        print("Regresaste a:", historial[-1])

    elif len(historial) == 1:
        # Si solo hay una página, no existe una anterior
        print("No puedes retroceder: no hay una página anterior.")

    else:
        # Si la pila está vacía, no hay páginas visitadas
        print("El historial está vacío.")

    # Mostramos cómo quedó la pila
    print("Pila actual:", historial)


def pagina_actual():
    # Verificamos si hay alguna página en la pila
    if historial:

        # Consultamos la última página sin eliminarla
        print("Página actual:", historial[-1])

    else:
        print("No hay una página actual.")


# Probamos las visitas en el orden indicado
visitar("Google")
visitar("YouTube")
visitar("GitHub")

# Consultamos la página actual sin quitarla
pagina_actual()

# Retrocedemos de GitHub a YouTube
retroceder()

# Retrocedemos de YouTube a Google
retroceder()

# Mostramos la página donde terminamos
pagina_actual()
