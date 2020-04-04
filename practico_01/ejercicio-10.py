# Implementar las funciones superposicion_x(), que tomen dos
# listas y devuelva un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    for i in lista_1:
        for j in lista_2:
            if i == j:
                return True
    return False


# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    set_1 = set(lista_1)
    set_2 = set(lista_2)
    setinterseccion = set_1.intersection(set_2)
    return len(setinterseccion) != 0


lista_1 = [1, 2]
lista_2 = [4, 3]
lista_3 = [5, "hola"]
lista_4 = ["hola", 4]

print(superposicion_loop(lista_1, lista_2))
print(superposicion_set(lista_3, lista_4))
