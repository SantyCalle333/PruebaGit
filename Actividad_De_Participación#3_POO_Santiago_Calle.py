import math

class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar(self):
        print(f"Coordenadas: ({self.x}, {self.y})")
    
    def mover(self, x, y):
        self.x = x
        self.y = y
    
    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)
        return distancia

class Rectangulo:
    def __init__(self, esquina1, esquina2):
        self.esquina1 = esquina1
        self.esquina2 = esquina2
    
    def calcular_perimetro(self):
        base = abs(self.esquina1.x - self.esquina2.x)
        altura = abs(self.esquina1.y - self.esquina2.y)
        return 2 * (base + altura)
    
    def calcular_area(self):
        base = abs(self.esquina1.x - self.esquina2.x)
        altura = abs(self.esquina1.y - self.esquina2.y)
        return base * altura
    
    def es_cuadrado(self):
        base = abs(self.esquina1.x - self.esquina2.x)
        altura = abs(self.esquina1.y - self.esquina2.y)
        return base == altura

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio**2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def punto_pertenece(self, punto):
        distancia_centro = self.centro.calcular_distancia(punto)
        return distancia_centro <= self.radio

class Carta:
    PINTAS = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance
    
    def depositar(self, cantidad):
        self.balance += cantidad
    
    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
        else:
            print("Fondos insuficientes.")
    
    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
    
    def mostrar_detalles(self):
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Balance: ${self.balance}")
        
# Datos De Prueba
v = Vehiculo(120, 50000)
print(v.velocidad_maxima)  # Salida: 120
print(v.kilometraje)        # Salida: 50000

p1 = Punto(0, 0)
p2 = Punto(3, 4)
p1.mostrar()                # Salida: Coordenadas: (0, 0)
print(p1.calcular_distancia(p2))  # Salida: 5.0

rectangulo = Rectangulo(Punto(0, 0), Punto(3, 3))
print(rectangulo.calcular_perimetro())  # Salida: 12
print(rectangulo.es_cuadrado())        # Salida: True

circulo = Circulo(Punto(0, 0), 5)
print(circulo.calcular_area())          # Salida: 78.53981633974483
print(circulo.punto_pertenece(Punto(3, 4)))  # Salida: True

carta = Carta(10, 'Corazones')
print(carta.valor)  # Salida: 10
print(carta.pinta)  # Salida: Corazones

cuenta = CuentaBancaria("123456", ["Juan", "María"], 1000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.aplicar_cuota_manejo()
cuenta.mostrar_detalles()
