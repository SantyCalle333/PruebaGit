#3 Generar lista de números aleatorios:

import random

cantidad_numeros = int(input("Ingrese la cantidad de números aleatorios a generar: "))
numeros_aleatorios = [random.randint(1, 100) for _ in range(cantidad_numeros)]
print("Lista de números aleatorios:", numeros_aleatorios)
