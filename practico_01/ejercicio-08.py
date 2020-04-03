# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
import math

def mitad(palabra):
    mitad = math.ceil(len(palabra)/2)
    mitadpalabra=""
    for i in range(mitad):
        mitadpalabra=mitadpalabra+palabra[i]
    return mitadpalabra

print(mitad("hola"))