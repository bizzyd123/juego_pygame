import pygame
from configuraciones import reescalar_imagenes, girar_imagenes
class AtaqueDistancia(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad,direccion,tipo):
        super().__init__()
        self.velocidad = velocidad
        self.tipo = tipo
        self.animaciones = self.__crear_animacion()
        self.reescalar_animaciones()
        self.direccion = direccion
        self.rect = self.animaciones[self.direccion][0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.contador_movimiento = 0

    
    def __crear_animacion_prota(self):
        personaje_ataca_distancia_derecha = [
            pygame.image.load("Recursos/Personaje/Distancia/1.png"),
            pygame.image.load("Recursos/Personaje/Distancia/2.png"),
            pygame.image.load("Recursos/Personaje/Distancia/3.png"),
            pygame.image.load("Recursos/Personaje/Distancia/4.png")
        ]
        personaje_ataca_distancia_izquierda = girar_imagenes(personaje_ataca_distancia_derecha,True,False)
        diccionario_animaciones={}
        diccionario_animaciones["derecha"] = personaje_ataca_distancia_derecha
        diccionario_animaciones["izquierda"] = personaje_ataca_distancia_izquierda
        return diccionario_animaciones
    
    def __crear_animacion_flecha(self):
        personaje_ataca_distancia_izquierda = [
            pygame.image.load("Recursos/Esqueleto/Distancia/1.png")
        ]
        personaje_ataca_distancia_derecha = girar_imagenes(personaje_ataca_distancia_izquierda,True,False)
        diccionario_animaciones={}
        diccionario_animaciones["derecha"] = personaje_ataca_distancia_derecha
        diccionario_animaciones["izquierda"] = personaje_ataca_distancia_izquierda
        return diccionario_animaciones
    
    
    def __crear_animacion_fuego(self):
        personaje_ataca_distancia_derecha = [
            pygame.image.load("Recursos/Brujo/Distancia/1.png")
        ]
        personaje_ataca_distancia_izquierda = girar_imagenes(personaje_ataca_distancia_derecha,True,False)
        diccionario_animaciones={}
        diccionario_animaciones["derecha"] = personaje_ataca_distancia_derecha
        diccionario_animaciones["izquierda"] = personaje_ataca_distancia_izquierda
        return diccionario_animaciones
    
    
    def __crear_animacion_magia(self):
        personaje_ataca_distancia_derecha = [
            pygame.image.load("Recursos/Mago/Distancia/1.png")
        ]
        personaje_ataca_distancia_izquierda = girar_imagenes(personaje_ataca_distancia_derecha,True,False)
        diccionario_animaciones={}
        diccionario_animaciones["derecha"] = personaje_ataca_distancia_derecha
        diccionario_animaciones["izquierda"] = personaje_ataca_distancia_izquierda
        return diccionario_animaciones
    
    def __crear_animacion(self):
        match self.tipo:
            case "esqueleto":
                animaciones = self.__crear_animacion_flecha()
            case "mago":
                animaciones = self.__crear_animacion_magia()
            case "brujo":
                animaciones = self.__crear_animacion_fuego()
            case _:
                animaciones = self.__crear_animacion_prota()
        return animaciones    
    
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave],  (40, 50))
    
    def update(self,pantalla):
        if self.direccion == "derecha":
            self.rect.x += self.velocidad
            self.animar(pantalla,self.direccion)
        else:
            self.rect.x += self.velocidad*-1
            self.animar(pantalla,self.direccion)
            
        
    def animar(self, pantalla: pygame.surface, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_movimiento >= largo:
            self.contador_movimiento = 0
        pantalla.blit(animacion[self.contador_movimiento], self.rect)
        self.contador_movimiento += 1