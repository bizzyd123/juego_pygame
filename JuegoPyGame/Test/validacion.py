import sqlite3
#archivo utilizado para validar el insert efectivo en la bd 
def ver_contenido_bd(nombre_bd):
    conexion = sqlite3.connect(nombre_bd)
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM puntajes")
    registros = cursor.fetchall()

    for registro in registros:
        print(registro)

    conexion.close()

ver_contenido_bd("puntajes.db")