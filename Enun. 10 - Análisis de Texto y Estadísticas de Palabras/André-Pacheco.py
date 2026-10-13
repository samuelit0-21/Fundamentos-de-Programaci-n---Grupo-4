import re

parrafo = """
Python es un lenguaje de programación potente. Python es fácil de aprender y 
programar en Python es rápido y divertido!
"""

palabras = re.findall(r"\b[a-zA-ZáéíóúÁÉÍÓÚñÑ']+\b", parrafo)

frecuencia = {}
for p in palabras:
    p_lower = p.lower()
    frecuencia[p_lower] = frecuencia.get(p_lower, 0) + 1

palabras_ordenadas = sorted(
    frecuencia.items(),
    key=lambda x: (-x[1], x[0])
)
top_5 = palabras_ordenadas[:5]
unicas = sorted(list(frecuencia.keys()))

print("=== TOP 5 PALABRAS MÁS FRECUENTES ===")
for palabra, freq in top_5:
    print(f"- '{palabra}': {freq} veces")

print("\n=== PALABRAS ÚNICAS (ORDENADAS ALFABÉTICAMENTE) ===")
print(unicas)
