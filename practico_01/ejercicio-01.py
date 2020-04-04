# 1. Implementar una función max() que tome como argumento dos números y
# devuelva el mayor de ellos


def maximo(a, b):
    return max(a, b)

# si no falla es porque esta bien


assert maximo(10, 5) == 10

assert maximo(9, 18) == 18

assert maximo(9, 9) == 9

assert maximo(9, 11) == 11
