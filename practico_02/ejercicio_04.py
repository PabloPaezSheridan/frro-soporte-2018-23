# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).
import ejercicio_03
from ejercicio_03 import Persona 
import datetime

class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        Persona.__init__(self, nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        return self.cantidad_aprobadas*100/self.cantidad_materias

    # implementar usando modulo datetime
    def edad_ingreso(self):
        now = datetime.datetime.now()
        return now.year - self.anio

#e1 = Estudiante("John Wick",34,"M",80,1.80,"Isi",4,42,22)
#print(e1.avance())
#print(e1.edad_ingreso())
