import pygame
from class_personaje import *
class ElementoGrafico(pygame.sprite.Sprite):
    
    def __init__(self, x,y, width, height,nombre_elemento):
        super().__init__()
        self.image = pygame.image.load(f"Recursos/ElementosGraficos/{nombre_elemento}.png")
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y    
        
    def ajustar_tamanio_rectangulo(self, new_width, new_height):
        old_center = self.rect.center
        self.rect.width = new_width
        self.rect.height = new_height
        self.rect.center = old_center