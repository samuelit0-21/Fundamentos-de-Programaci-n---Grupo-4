# Importamos nuestro módulo propio con el alias 'mu' tal como se solicita
import matematicas_utils as mu

def reporte_geometrico(radios):
    
    # Función que recibe una lista de radios y muestra en una tabla 
    # el radio, el área y el perímetro de cada círculo calculado.
    
    # Imprimimos la cabecera de la tabla con anchos de columna fijos para mayor prolijidad
    print(f"{'Radio':<10} | {'Área':<15} | {'Perímetro':<15}")
    print("-" * 46)
    
    # Iteramos a través de cada elemento (radio) dentro de la lista 'radios'
    for r in radios:
        # Usamos el módulo con el alias 'mu' para calcular el área llamando a su función
        area = mu.area_circulo(r)
        
        # Usamos el módulo con el alias 'mu' para calcular el perímetro llamando a su función
        perimetro = mu.perimetro_circulo(r)
        
        # Imprimimos los valores formateados a 2 decimales dentro de la tabla
        print(f"{r:<10} | {area:<15.2f} | {perimetro:<15.2f}")

# Bloque de ejecución principal
if __name__ == "__main__":
    # Definimos una lista de prueba con diferentes valores de radios
    radios_prueba = [1, 4, 5.5, 10]
    
    print("REPORTE GEOMÉTRICO DE CÍRCULOS")
    print("-" * 46)
    # Llamamos a la función reporte_geometrico pasando la lista de radios
    reporte_geometrico(radios_prueba)
