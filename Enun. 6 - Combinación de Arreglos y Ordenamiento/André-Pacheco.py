productos = ["Laptop", "Mouse", "Teclado", "Monitor"]
ventas = [150, 450, 300, 200]

combinados = [{"nombre": p, "ventas": v} for p, v in zip(productos, ventas)]

combinados.sort(key=lambda x: x["ventas"], reverse=True)

print("=== RANKING DE VENTAS ===")
for idx, item in enumerate(combinados, 1):
    print(f"{idx}° Lugar: {item['nombre']:<10} - Ventas: {item['ventas']}")

promedio_ventas = sum(ventas) / len(ventas)
print(f"\nPromedio general de ventas: {promedio_ventas:.2f}")
print("Productos sobre la media:")
for item in combinados:
    if item["ventas"] > promedio_ventas:
        print(f" -> {item['nombre']} ({item['ventas']} ventas)")
