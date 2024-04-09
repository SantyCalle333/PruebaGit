from dataclasses import dataclass
from typing import List

@dataclass(eq=True, frozen=True)
class Elemento:
    nombre: str

@dataclass
class Conjunto:
    contador = 0

    def __init__(self, nombre: str):
        self.elementos: List[Elemento] = []
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento: Elemento) -> bool:
        return elemento in self.elementos

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        for elemento in self.elementos + otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def unir(self, otro_conjunto):
        return self + otro_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre_interseccion = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        interseccion = Conjunto(nombre_interseccion)
        for elemento in conjunto1.elementos:
            if conjunto2.contiene(elemento):
                interseccion.agregar_elemento(elemento)
        return interseccion

    def __str__(self):
        elementos_str = ', '.join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"

# Crear elementos
elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")

# Crear conjuntos
conjunto1 = Conjunto("Conjunto1")
conjunto2 = Conjunto("Conjunto2")

# Agregar elementos a conjuntos
conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

# Unir conjuntos
union = conjunto1.unir(conjunto2)
print(union)

# Intersectar conjuntos
interseccion = Conjunto.intersectar(conjunto1, conjunto2)
print(interseccion)
