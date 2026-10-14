# Creamos la lista de nombres.
nombres = ["Carlos", "ana", "Beatriz", "david", "Elena"]

# Mostramos la lista antes de modificarla.
print("Lista original:", nombres)

# sort() ordena la misma lista.
# key=str.lower compara los nombres como si estuvieran en minúsculas.
# Los nombres conservan su escritura original.
nombres.sort(key=str.lower)

# Mostramos la lista ordenada de A a Z.
print("Lista ascendente:", nombres)

# sorted() crea una nueva lista ordenada.
# reverse=True indica que el orden será de Z a A.
descendente = sorted(nombres, key=str.lower, reverse=True)

# Mostramos la nueva lista.
print("Nueva lista descendente:", descendente)

# Comprobamos que sorted() no cambió la lista nombres.
print("Lista nombres después de sorted():", nombres)
