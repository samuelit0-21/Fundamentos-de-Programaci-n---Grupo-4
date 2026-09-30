#ORDENAR NOTAS ESTUDIANTILES
#Un profesor tiene las notas de 6 estudiantes en una lista desordenada:
notas=[85, 42, 93, 67, 28, 75]

#Se pide:
#a) Ordenar la lista usando
#Bubble Sort e imprimir el resultado.
#b) Ordenar usando
#Selection Sort e imprimir el resultado.
#c) Mostrar la nota mínima, máxima y el promedio

def burbuja(lista):
    n=len(lista)
    for i in range (n):                    
            intercambiado = False               
            for j in range(0,n-i-1):        
                if lista[j]>lista[j+1]:        
                    lista[j],lista[j+1] = lista[j+1],lista[j]   
                    intercambiado = True        
            if not intercambiado:              
                break                           

burbuja(notas)
print(notas)
notas = 0


def seleccion(lista):
    n=len(lista)                                                   
    for i in range(n - 1):                                          
        idx_min=i                                                          
        for j in range(i+1,n):                                     
            if lista[j]<lista[idx_min]:                                     
                idx_min = j                                         
        if idx_min !=i:
            lista[i],lista[idx_min] = lista[idx_min], lista[i]

notas= [85,42,93,67,28,75]

seleccion(notas)
print(notas)

print(min(notas))
print(max(notas))
promedio = sum(notas)/len(notas)
print(promedio)
