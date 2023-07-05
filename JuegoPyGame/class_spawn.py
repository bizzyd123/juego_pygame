from class_elementografico import * 
from class_enemigo import *
class Spawn(ElementoGrafico):
    def __init__(self, x,y, width, height,nombre_elemento,nombre_enemigo, vida_enemigos,daño_enemigos, pos_inicial = (720, 350)):
        super().__init__(x,y,width,height,nombre_elemento)
        
        self.spawn_activo = False
        self.nombre_enemigo = nombre_enemigo
        self.vida_enemigos = vida_enemigos
        self.daño_enemigos = daño_enemigos
        self.pos_inicial = pos_inicial
        
    def activar_spawn(self, mi_personaje,enemigos_grupo):
        """brief: verifica la colision del rectangulo spawn con el personaje principal
        si hay colision entonces se carga el grupo de enemigos
        parameters: self
        return: None"""
        if not self.spawn_activo:  # Verificar si el spawn no está activo
            if self.rect.colliderect(mi_personaje.rect):
                enemigos_grupo.add(Enemigo((75, 85), self.pos_inicial, 4, self.vida_enemigos, 1,self.nombre_enemigo,self.daño_enemigos,20,200))
                self.spawn_activo = True

        if self.spawn_activo:  # Verificar si el spawn está activo
            if not self.rect.colliderect( mi_personaje.rect):
                self.spawn_activo = False