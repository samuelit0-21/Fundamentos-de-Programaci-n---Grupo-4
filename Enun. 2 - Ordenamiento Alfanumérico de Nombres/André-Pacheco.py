nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']

print("1) Original:", nombres)

nombres_copia = nombres.copy()
nombres_copia.sort(key=str.lower)
print("2) Orden ascendente (sin importar mayúsculas):", nombres_copia)

nombres_desc = sorted(nombres, key=str.lower, reverse=True)

print("3) Orden descendente:", nombres_desc)
