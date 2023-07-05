import json

class GrabadorExcepciones:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def leer_archivo(self):
        """brief: hago la apertura del archivo y retorno una lista del contenido
        parameters: 
        return: None
        """
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                excepciones_guardadas = json.load(archivo)
        except FileNotFoundError:
            excepciones_guardadas = []
        return excepciones_guardadas
    
    def escribir_excepcion(self, excepcion):
        """brief: se le da formato a la excepcion para ser guardada en el archivo.
        parameters: excepcion
        return: None
        """
        excepciones_guardadas = self.leer_archivo()

        excepcion_dict = {
            "tipo": type(excepcion).__name__,
            "mensaje": str(excepcion)
        }
        excepciones_guardadas.append(excepcion_dict)
        self.guardar_json(excepciones_guardadas)
        
    def guardar_json(self,excepciones_guardadas):
        """brief: guarda en un archivo la lista de excepciones recibidas
        parameters:excepciones_guardadas
        return: None
        """
        with open(self.nombre_archivo, 'w') as archivo:
            json.dump(excepciones_guardadas, archivo, indent=4)
