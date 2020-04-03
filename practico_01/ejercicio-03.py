# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operacion(a, b, multiplicar):
    if(b == 0):
        return "Operacion no valida"
    if (multiplicar=='true'):
        return a*b
    if(multiplicar == 'false', b != 0):
        return a/b


    pass

print(operacion(2,3,'true'))
print(operacion(2,3,'false'))
print(operacion(2,0,'true'))