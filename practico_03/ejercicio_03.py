# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import sqlite3

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    conexion = sqlite3.connect("sgdpv.db")
    cursor = conexion.cursor()
    values = (id_persona,)
    sql = ("DELETE FROM persona WHERE IdPersona = ?;")
    resultado = cursor.execute(sql, values).rowcount
    conexion.commit()
    conexion.close()
    if resultado > 0:
        return True
    return False


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
