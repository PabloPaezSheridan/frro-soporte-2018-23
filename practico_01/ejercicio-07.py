
# Implementar la función numeros_al_final(), que mueve
# todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(len(lista)):
        if lista[i] in numeros:
            lista.append(lista[i])
            lista.pop(i)
    return lista

# para python viejito
# def numeros_al_final(lista):
#    lista.sort(reverse=True)


lista = ["n", 0, "p", 1, "a"]
print(numeros_al_final(lista))
