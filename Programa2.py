#2 Calcular área de un círculo:

import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

radio = float(input("Ingrese el radio del círculo: "))
print("El área del círculo es:", calcular_area_circulo(radio))
