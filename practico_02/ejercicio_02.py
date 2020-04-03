# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.
import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        return math.pi * (self.radio**2)         

    def perimetro(self):
        return 2 * math.pi * self.radio


c1 = Circulo(3)
print(c1.area())
print(c1.perimetro())
