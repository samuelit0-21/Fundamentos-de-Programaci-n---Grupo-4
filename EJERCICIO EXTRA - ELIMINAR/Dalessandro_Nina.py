# Creamos una lista donde "uva" aparece dos veces
frutas = ["uva", "pera", "uva", "maracuyá"]

# Esta variable cuenta cuántas veces encontramos "uva"
contador = 0

# Recorremos la lista utilizando sus índices: 0, 1, 2 y 3
for i in range(len(frutas)):

    # Verificamos si la fruta del índice actual es "uva"
    if frutas[i] == "uva":

        # Aumentamos el contador en uno
        contador += 1

        # Si encontramos "uva" por segunda vez
        if contador == 2:

            # Eliminamos la fruta ubicada en ese índice
            del frutas[i]

            # Terminamos el recorrido después de eliminarla
            break

# Mostramos la lista después de eliminar la segunda "uva"
print(frutas)
