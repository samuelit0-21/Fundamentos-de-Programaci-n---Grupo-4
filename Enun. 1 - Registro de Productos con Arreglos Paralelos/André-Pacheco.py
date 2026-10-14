nombres = ["Laptop", "Mouse", "Teclado", "Monitor"]
precios = [2500.0, 50.0, 120.0, 600.0]
cantidades = [5, 20, 15, 8]

total_inventario = 0

print("=== REPORTE DE INVENTARIO ===")
for i in range(len(nombres)):
    subtotal = precios[i] * cantidades[i]
    total_inventario += subtotal
    print(f"Producto: {nombres[i]:<10} | Precio: S/.{precios[i]:<7.2f} | Stock: {cantidades[i]:<3} | Subtotal: S/.{subtotal:.2f}")

print("-" * 60)
print(f"Valor total del inventario: S/.{total_inventario:.2f}")
