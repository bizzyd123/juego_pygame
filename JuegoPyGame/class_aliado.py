from configuraciones import reescalar_imagenes
from class_item import *
class Aliado(pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.animaciones = self.__crear_animacion()
        self.reescalar_animaciones()
        self.spawn_activo = False
        self.rect = self.animaciones["quieto"][0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.contador_movimiento = 0
    def __crear_animacion(self):
        personaje_quieto = [
            pygame.image.load("Recursos/Trotuman/Quieto/1.png"),
            pygame.image.load("Recursos/Trotuman/Quieto/2.png"),
            pygame.image.load("Recursos/Trotuman/Quieto/3.png")
        ]
        diccionario_animaciones={}
        diccionario_animaciones["quieto"] = personaje_quieto
        return diccionario_animaciones
    
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave],  (75, 85))
            
    def activar_spawn(self, mi_personaje,items_group):
        """brief: verifica la colision del rectangulo del aliado
        con el personaje principal
        si hay colision entonces se  genera items de ayuda
        parameters: self
        return: None"""
        if not self.spawn_activo:  # Verificar si el spawn no está activo
            if self.rect.colliderect(mi_personaje.rect):
                items_group.add(Item(self.rect.right+10,self.rect.centery,20,20,"vida","item_vida",10))
                items_group.add(Item(self.rect.right+20,self.rect.centery,40,40,"magia","item_magia",5))
                self.spawn_activo = True
                
                
    def update(self,pantalla, mi_personaje,items_group):
        self.animar(pantalla,"quieto")
        self.activar_spawn( mi_personaje,items_group)
            
        
    def animar(self, pantalla: pygame.surface, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_movimiento >= largo:
            self.contador_movimiento = 0
        pantalla.blit(animacion[self.contador_movimiento], self.rect)
        self.contador_movimiento += 1