#1 Pedir nombre y edad:

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print("Nombre:", nombre)
print("Edad:", edad)

#2 Calcular área de un círculo:

import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

radio = float(input("Ingrese el radio del círculo: "))
print("El área del círculo es:", calcular_area_circulo(radio))

#3 Generar lista de números aleatorios:

import random

cantidad_numeros = int(input("Ingrese la cantidad de números aleatorios a generar: "))
numeros_aleatorios = [random.randint(1, 100) for _ in range(cantidad_numeros)]
print("Lista de números aleatorios:", numeros_aleatorios)

#4 Determinar si un número es par o impar:

def par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = int(input("Ingrese un número: "))
print("El número es", par_o_impar(numero))

#5 Convertir grados Fahrenheit a Celsius:

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
print("La temperatura en grados Celsius es:", fahrenheit_a_celsius(fahrenheit))

#6 Calcular la suma de los números en una lista:

def suma_lista(lista):
    return sum(lista)

numeros = [1, 2, 3, 4, 5]  # Ejemplo de lista
print("La suma de los números en la lista es:", suma_lista(numeros))


#7 Encontrar el número más grande y más pequeño en una lista:

def encontrar_extremos(lista):
    return min(lista), max(lista)

numeros = [1, 5, 3, 7, 9]  # Ejemplo de lista
minimo, maximo = encontrar_extremos(numeros)
print("El número más pequeño es:", minimo)
print("El número más grande es:", maximo)

#8 Invertir el orden de los elementos en una lista:

def invertir_lista(lista):
    return lista[::-1]

numeros = [1, 2, 3, 4, 5]  # Ejemplo de lista
print("Lista invertida:", invertir_lista(numeros))

#9 Generar matriz de números:

import numpy as np

filas = int(input("Ingrese el número de filas: "))
columnas = int(input("Ingrese el número de columnas: "))
matriz = np.random.randint(1, 100, size=(filas, columnas))
print("Matriz generada:")
print(matriz)

#10 Calcular el factorial de un número:

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Ingrese un número: "))
print("El factorial de", numero, "es:", factorial(numero))

#11 Generar lista de números pares entre 1 y 100:

numeros_pares = [num for num in range(1, 101) if num % 2 == 0]
print("Lista de números pares entre 1 y 100:", numeros_pares)

#12 Imprimir números del 1 al 10 utilizando un ciclo for:

for i in range(1, 11):
    print(i)

#13 Calcular suma, resta, multiplicación y división de dos números:

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre 0"

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

#14 Calcular la media aritmética de una lista de números:

def media_aritmetica(lista):
    return sum(lista) / len(lista)

numeros = [1, 2, 3, 4, 5]  # Ejemplo de lista
print("La media aritmética de la lista es:", media_aritmetica(numeros))

#15 Determinar si una cadena de texto es un palíndromo:

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    return cadena == cadena[::-1]

texto = input("Ingrese una cadena de texto: ")
if es_palindromo(texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
