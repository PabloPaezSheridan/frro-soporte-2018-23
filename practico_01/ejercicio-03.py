# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por
# consola "Operación no valida".


def operacion(a: int, b:int, multiplicar: bool) -> int:
    if multiplicar:
        return a * b
    else:
        if b == 0:
            return "Operación no valida"
        return a/b


print(operacion(4, 2, False))
print(operacion(2, 3, True))
print(operacion(2, 3, False))
print(operacion(2, 0, False))