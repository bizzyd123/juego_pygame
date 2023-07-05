import pygame
import pygame.mixer
class Nivel:
    def __init__(self,personaje_grupo:pygame.sprite.Group,enemigos_grupo,plataformas_grupo,
                 trampas_grupo,item_grupo,spawn_grupo,
                 fondo:str, musica:str, TAMAÑO_PANTALLA:tuple, jefe,
                 aliado_grupo = None,hay_aliado = False):
        if aliado_grupo is None:
            aliado_grupo = pygame.sprite.Group()
        self.personaje_grupo = personaje_grupo
        self.enemigos_grupo = enemigos_grupo
        self.plataformas_grupo = plataformas_grupo
        self.trampas_grupo = trampas_grupo
        self.item_grupo = item_grupo
        self.spawn_grupo = spawn_grupo
        self.spawn_activo = False
        self.fondo =  pygame.image.load(f"Recursos/Fondos/{fondo}.png")
        self.fondo = pygame.transform.scale(self.fondo,TAMAÑO_PANTALLA)
        self.fondo_rect = self.fondo.get_rect()
        self.tiempo_maximo =  60
        self.mi_personaje = personaje_grupo.sprites()[0]
        self.PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
        self.jefe = jefe
        self.musica = musica
        self.aliado_grupo = aliado_grupo
        self.hay_aliado = hay_aliado