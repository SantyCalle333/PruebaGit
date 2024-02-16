#10 Calcular el factorial de un número:

def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = int(input("Ingrese un número: "))
print("El factorial de", numero, "es:", factorial(numero))
