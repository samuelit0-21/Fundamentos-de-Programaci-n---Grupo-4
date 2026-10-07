tweet = "Aprendiendo #Python y #Programacion en el curso de #Sistemas con #python"

palabras = tweet.split()
hashtags = []

for palabra in palabras:
    if palabra.startswith("#"):
        tag_limpio = palabra.lower()
        if tag_limpio not in hashtags:  #evitando duplicados
            hashtags.append(tag_limpio)

hashtags.sort()
print("Hashtags encontrados:", hashtags)
