# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from ejercicio_01 import borrar_tabla, crear_tabla
import sqlite3


def crear_tabla_peso():
    conexion = sqlite3.connect("sgdpv.db")
    cursor = conexion.cursor()
    try:
        sql = ("""CREATE TABLE IF NOT EXISTS PersonaPeso (
            IdPersona INTEGER,
            Fecha TEXT,
            PESO INTEGER,
            PRIMARY KEY(IdPersona,Fecha),
            FOREIGN KEY(IdPersona) REFERENCES persona(IdPersona)
            );""")
        cursor.execute(sql)
        conexion.commit()
    finally:
        conexion.close()
    pass


def borrar_tabla_peso():
    def borrar_tabla():
        conexion = sqlite3.connect("sgdpv.db")
        cursor = conexion.cursor()
        sql = ("DROP TABLE IF EXISTS PersonaPeso")
        cursor.execute(sql)
        conexion.commit()
        conexion.close()
    pass


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
