# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
#round no funciona
def mitad(palabra):
    lon = (len(palabra))
    if lon % 2 == 0:
        mitad = lon // 2
        return palabra[:mitad]
    mitad = lon // 2 + 1
    return palabra[:mitad]


print(mitad("hola"))
print(mitad("cosas"))
print(mitad("verde"))
