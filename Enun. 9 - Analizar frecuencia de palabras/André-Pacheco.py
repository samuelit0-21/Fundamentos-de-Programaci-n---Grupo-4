def analizar_frecuencia(texto):
    stopwords = ["de", "con", "el", "la", "en", "y", "a", "un", "una"]
    
    #Eliminando signos de puntuación
    for signo in [".", ",", ";", ":", "!", "?"]:
        texto = texto.replace(signo, "")
    
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        if palabra not in stopwords:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
            
    return frecuencias

parrafo = "Python es un lenguaje de programación. Python es rápido y fácil de aprender en programación."
print("Frecuencia de palabras:", analizar_frecuencia(parrafo))
