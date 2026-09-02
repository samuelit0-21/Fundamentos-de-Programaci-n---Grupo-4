#Recorremos un rango de números, por cada par, le incrementamos al contador y acumulamos la suma de los números pares
Contador = 0
Suma_pares = 0
for i in range(1,21):
    if i % 2 == 0:
        Contador += 1
        Suma_pares += i

print("Cantidad de números pares:", Contador)

print("Suma de los números pares:", Suma_pares) 

print("La cantidad de números pares es:", Contador, "y la suma de los números pares es:", Suma_pares)