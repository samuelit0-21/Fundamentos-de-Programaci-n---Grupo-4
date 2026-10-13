import re

datos_raw = [
    'Ana García - edad:25 - tel:987654321',
    'Luis Pérez - edad:30 - tel:912345678'
]

patron = r'^(?P<nombre>[\w\s]+)\s*-\s*edad:(?P<edad>\d+)\s*-\s*tel:(?P<telefono>\d+)'
registros = []

for item in datos_raw:
    match = re.search(patron, item)
    if match:
        data = match.groupdict()
        data["edad"] = int(data["edad"])
        registros.append(data)

print("=== DATOS EXTRAÍDOS ===")
for r in registros:
    print(r)
