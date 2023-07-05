from class_elementografico import * 
class Item(ElementoGrafico):
    def __init__(self, x,y, width, height,nombre_elemento, tipo:str, efecto:int):
        super().__init__(x,y, width, height,nombre_elemento)
        self.tipo = tipo
        self.efecto = efecto
    