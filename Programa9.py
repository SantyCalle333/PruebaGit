#9 Generar matriz de números:

import numpy as np

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz = np.random.randint(1, 100, size=(filas, columnas))
print("Matriz generada:")
print(matriz)
