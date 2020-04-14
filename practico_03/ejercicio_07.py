# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3
from ejercicio_02 import agregar_persona
from ejercicio_04 import buscar_persona
from ejercicio_06 import reset_tabla, crear_tabla_peso


def agregar_peso(id_persona, fecha, peso):
    if not buscar_persona(id_persona):
        return False
    conexion = sqlite3.connect("sgdpv.db")
    cursor = conexion.cursor()
    values = (id_persona,)
    sql = ("SELECT Fecha FROM PersonaPeso WHERE IdPersona = ?;")
    resultado = cursor.execute(sql, values).fetchall()
    for row in resultado:
        if datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") >= fecha:
            return False
    sql = ("INSERT INTO PersonaPeso (IdPersona,Fecha,PESO) VALUES (?, ?, ?)")
    values = (id_persona, fecha, peso)
    cursor.execute(sql, values)
    conexion.commit()
    id_ = cursor.lastrowid
    conexion.close()
    return id_


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    print(id_juan)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False


if __name__ == '__main__':
    pruebas()
