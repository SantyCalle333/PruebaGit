#5 Convertir grados Fahrenheit a Celsius:

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
print("La temperatura en grados Celsius es:", fahrenheit_a_celsius(fahrenheit))
