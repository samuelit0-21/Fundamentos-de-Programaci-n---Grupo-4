frutas = ["uva", "pera", "uva", "maracuja"]

contador = 0

for i in range(len(frutas)):
    if frutas[i] == "uva":
        contador += 1

        if contador == 2:
            del frutas[i]
            break

print(frutas)
