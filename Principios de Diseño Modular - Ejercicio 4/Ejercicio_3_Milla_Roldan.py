def leer_datos(fuente):
    return [1, -2, 3, -4, 5]
def filtrar_positivos(datos):
    return [x for x in datos if x > 0]
def calcular_estadisticas(datos):
    return {
"suma": sum(datos),
"media": sum(datos) / len(datos),
"max": max(datos)
}
# Pipeline modular
datos = leer_datos("archivo.csv")
limpios = filtrar_positivos(datos)
stats = calcular_estadisticas(limpios)
print(stats)
# {'suma': 9, 'media': 3.0, 'max': 5}
