# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from ejercicio_04 import Estudiante

e1 = Estudiante("John Wick",34,"M",80,1.80,"Isi",4,42,22)
e2 = Estudiante("John Wick",34,"M",80,1.80,"Qmc",4,42,22)
e3 = Estudiante("John Wick",34,"M",80,1.80,"Mec",4,42,22)
e4 = Estudiante("John Wick",34,"M",80,1.80,"Qmc",4,42,22)
e5 = Estudiante("John Wick",34,"M",80,1.80,"Isi",4,42,22)
e6 = Estudiante("John Wick",34,"M",80,1.80,"Isi",4,42,22)

estudiantes = [e1, e2, e3, e4, e5, e6]


def organizar_estudiantes(estudiantes):
    Dictionary1 = {} 
    for e in estudiantes:
        if e.carrera not in Dictionary1.keys():
            Dictionary1[e.carrera] = 1
        else:
            Dictionary1[e.carrera] = Dictionary1[e.carrera] + 1
    return Dictionary1


print(organizar_estudiantes(estudiantes))

