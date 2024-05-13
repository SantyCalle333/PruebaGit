#7 Encontrar el número más grande y más pequeño en una lista:

def encontrar_extremos(lista):
    return min(lista), max(lista)

numeros = [1, 5, 3, 7, 9]  # Ejemplo de lista
minimo, maximo = encontrar_extremos(numeros)
print("El número más pequeño es:", minimo)
print("El número más grande es:", maximo)
