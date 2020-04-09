# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3


def crear_tabla():
    conexion = sqlite3.connect("sgdpv.db")
    cursor = conexion.cursor()
    sql = ("""CREATE TABLE IF NOT EXISTS persona (
        IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre TEXT,
        FechaNacimiento TEXT,
        DNI INTEGER,
        Altura INTEGER
        );""")
    cursor.execute(sql)
    conexion.commit()
    conexion.close()
    pass


def borrar_tabla():
    conexion = sqlite3.connect("sgdpv.db")
    cursor = conexion.cursor()
    sql = ("DROP TABLE IF EXISTS persona")
    cursor.execute(sql)
    conexion.commit()
    conexion.close()
    pass


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

# import mysql.connector

# dbConnect = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'root',
#     'database': 'sgdpv'
# }


# resultados = cursor.execute(sql)


# cursor.execute(sql)

# for datos in resultados:
#     print(str(datos[0]+" "+str(datos[1])))