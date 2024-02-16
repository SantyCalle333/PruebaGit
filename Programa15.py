#15 Determinar si una cadena de texto es un palíndromo:

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios
    return cadena == cadena[::-1]

texto = input("Ingrese una cadena de texto: ")
if es_palindromo(texto):
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
