import sqlite3

class DataAccess:
    def __init__(self, nombre_bd='puntajes.db'):
        self.conexion = sqlite3.connect(nombre_bd)
        self.cursor = self.conexion.cursor()
        self.crear_tabla()

    def __del__(self):
        self.conexion.close()

    def crear_tabla(self):
        """brief: ejecuta una consulta sql para crear la tabla
        en caso de que no exista
        parameters:
        return:
        """
        #creamos tabla si no existe
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS puntajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                puntaje INTEGER NOT NULL
            )
        ''')
        #hacemos efectivo el cambio en la base de datos
        self.conexion.commit()

    def insertar_puntaje(self, nombre, puntaje):
        """brief: inserta el registro de nombre y puntaje en la tabla  de la base de datos
        paramters:
        return:"""
        #insertamos registro
        self.cursor.execute('INSERT INTO puntajes (nombre, puntaje) VALUES (?, ?)', (nombre, puntaje))
        #hacemos efectivo el cambio en la base de datos
        self.conexion.commit()

    def obtener_puntajes(self)-> dict:
        """brief: hace una consulta de los nombres y puntajes almacenados 
        pàrameters:
        return:
        
        """
        #escribo el query
        self.cursor.execute('SELECT nombre, puntaje FROM puntajes')
        #recupero registros de la consulta
        registros = self.cursor.fetchall()
        puntajes = []
        #itero los resultados para armar el diccionario de salida
        for nombre, puntaje in registros:
            puntaje_dict = {"nombre": nombre, "puntaje": puntaje}
            puntajes.append(puntaje_dict)

        return puntajes

