# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

import datetime

class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def edad(self):     
        hoy = datetime.date.today()
        if hoy < self.nacimiento:
            return 0
        else:
            ano = self.nacimiento.year
            mes = self.nacimiento.month
            dia = self.nacimiento.day

            fecha = self.nacimiento
            edad = 0
            while fecha < hoy:
                edad += 1
                fecha = datetime.date(ano+edad, mes, dia)

            return edad-1


fdn = datetime.date(1997, 6, 8)
p1 = Persona(fdn)
print(p1.edad())
