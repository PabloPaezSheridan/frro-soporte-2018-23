# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.
import random

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni()    

    def es_mayor_edad(self):
        return self.edad >= 18     

    # llamarlo desde __init__
    def generar_dni(self):
        return random.randint(10000000, 99999999)

    def print_data(self):
        print ("Nombre: ", self.nombre)
        print ("Edad: ", self.edad)
        print ("Sexo: ", self.sexo)
        print ("Peso: ", self.peso)
        print ("Altura: ", self.altura)
        print ("Dni: ", self.dni)

#p1 = Persona("John Wick",34,"M",80,1.80)
#p1.print_data()
#print(p1.es_mayor_edad())
