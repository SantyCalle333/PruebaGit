#4 Determinar si un número es par o impar:

def par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

numero = int(input("Ingrese un número: "))
print("El número es", par_o_impar(numero))
