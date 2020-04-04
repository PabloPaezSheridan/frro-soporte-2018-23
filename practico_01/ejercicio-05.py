# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.
def es_vocal(letra):
    vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return letra in vocales

    # for i in vocales:
    #    if i == letra:
    #        return True
    #    else:
    #        return False


print(es_vocal("b"))
print(es_vocal("a"))
print(es_vocal("I"))
print(es_vocal("T"))
