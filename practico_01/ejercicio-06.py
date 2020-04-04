
# Implementar la función multiplicar() que devuelva el producto de todos los
# números de una lista.


# [1,2,3,4] -> 24
def multiplicar(lista):
    if len(lista) == 0:
        return 0
    a = 1
    for i in lista:
        a = a * i
    return a


print(multiplicar([1, 2, 3, 4]))
print(multiplicar([]))
