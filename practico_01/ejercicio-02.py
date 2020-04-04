# Implementar la función mayor, que reciba tres números
# y devuelva el mayor de ellos.


def mayor(a, b, c):
    return max(a, b, c)


def mayor2(*args):
    return max(*args)        

# si no falla es porque esta bien


assert mayor(1, 10, 5) == 10
assert mayor(4, 9, 18) == 18
assert mayor2(4, 10, 5, 1, 7) == 10

print("hola")
