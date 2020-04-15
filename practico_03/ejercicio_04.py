# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

from datetime import datetime
from dateutil.parser import parse
import sqlite3

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona

def existe(id_persona):
    conexion = sqlite3.connect("sgdpv.db")
    cursor = conexion.cursor()
    values = (id_persona,)
    sql = ("  SELECT EXISTS(SELECT 1 FROM persona WHERE idPersona=? ); ")
    respuesta = cursor.execute(sql,values).fetchone()
    return 1 in respuesta



def buscar_persona(id_persona):
    conexion = sqlite3.connect("sgdpv.db")
    cursor = conexion.cursor()
    values = (id_persona,)
    sql = ("SELECT idPersona,Nombre,FechaNacimiento,DNI,Altura FROM persona WHERE IdPersona = ?;")
    resultado = cursor.execute(sql, values).fetchone()
    if not resultado:
        return False
    id_, nombre, fechanacimiento, dni, altura = resultado
    fechanacimiento = datetime.strptime(fechanacimiento, '%Y-%m-%d')
    conexion.close()
    return id_, nombre, fechanacimiento, dni, altura


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
