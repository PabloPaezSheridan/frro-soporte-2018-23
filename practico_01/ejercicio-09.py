# Implementar la función es_palindromo(), que devuelva un booleano en base a
# si palabra se lee igual de corrido como al revés.


# Ejemplos: arenera, radar, ojo, oso, salas.
# Resolver sin utilizar loops (for/while), sino con slicing.


def es_palindromo(palabra):
    dadavuelta = palabra[::-1]
    return dadavuelta == palabra


print(es_palindromo("arenera"))
print(es_palindromo("hola"))
print(es_palindromo("radar"))
print(es_palindromo("chau"))
print(es_palindromo("ojo"))
print(es_palindromo("juan"))
