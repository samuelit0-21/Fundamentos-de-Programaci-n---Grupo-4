def clasificar_temperatura(temp):
    
    # Clasifica una temperatura según los siguientes rangos:
    # - Frío: menor a 10
    # - Fresco: menor a 20
    # - Cálido: menor a 30
    # - Caliente: 30 o mayor
    
    # Se evalúan las condiciones de forma encadenada (elif)
    if temp < 10:
        # Temperatura menor a 10
        return "Frío"
    elif temp < 20:
        # Temperatura mayor o igual a 10 y menor a 20
        return "Fresco"
    elif temp < 30:
        # Temperatura mayor o igual a 20 y menor a 30
        return "Cálido"
    else:
        # Temperatura mayor o igual a 30
        return "Caliente"

# Pruebas.
print(clasificar_temperatura(5))    # Frío
print(clasificar_temperatura(15))   # Fresco
print(clasificar_temperatura(25))   # Cálido
print(clasificar_temperatura(30))   # Caliente
print(clasificar_temperatura(35))   # Caliente
