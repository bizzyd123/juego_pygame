import pygame, sys
from configuraciones import *
from pygame.locals import *
from class_protagonista import *
from class_elementografico import *
from class_spawn import *
from class_enemigo import *
from class_aliado import * 
from modo import *
from GUI_Menu import *
from class_item import *
import pygame.mixer
import time
from class_nivel import *
from class_archivos import *

class Game():
    def __init__(self, _lista_niveles: list[Nivel],W:int, H:int):
        self.index = 0
        self.ficheros = GrabadorExcepciones("excepciones.json")
        self.puntaje_final = 0
        self.game_over = False 
        self.jefe_activo = False
        self.TAMAÑO_PANTALLA = (W,H)
        self.FPS = 18
        self.esPausa = False
        pygame.init()
        self.RELOJ = pygame.time.Clock()
        self.lista_niveles  = _lista_niveles
        pygame.mixer.init()
        self.establecer_nivel(self.index)
        self.fuente = pygame.font.Font("Recursos/Fuente/fuente.ttf", 28)
        self.form_menu = GUI_Menu(self.PANTALLA,200,100,900,350,self,self.musica,(0, 255, 255),"Magenta",5,True)
     
        
    def establecer_nivel(self, indice:int):
        """Brief: permite establecer los atributos necesarios para el nivel actual del juego
        grupos de sprites, fondos, tiempo maximo, personaje principal, enemigos, jefe
        parameters: self
        return:  None
        """
        if indice < len(self.lista_niveles):
            nivel = self.lista_niveles[indice]
            self.personaje_grupo = nivel.personaje_grupo
            self.enemigos_grupo = nivel.enemigos_grupo
            self.plataformas_grupo = nivel.plataformas_grupo
            self.trampas_grupo = nivel.trampas_grupo
            self.item_grupo = nivel.item_grupo
            self.spawn_grupo = nivel.spawn_grupo
            self.spawn_activo = False
            self.fondo =  nivel.fondo
            self.fondo_rect = nivel.fondo_rect
            self.tiempo_maximo = nivel.tiempo_maximo
            self.mi_personaje = nivel.mi_personaje
            self.PANTALLA = nivel.PANTALLA
            self.jefe = nivel.jefe
            self.musica = nivel.musica
            self.aliado_grupo = nivel.aliado_grupo
            self.hay_aliado = nivel.hay_aliado
            self.time = time.time()
            
        else : 
            text = self.fuente.render(f"Juego completado",True,(255,0,0))
            self.PANTALLA.blit(text, (675, 350))
            self.RELOJ.tick(0)
            pygame.display.update()
            pygame.time.delay(5000)
            self.game_over = True
    
    def RunGame(self):
        try:
            while not self.game_over:
                
                self.RELOJ.tick(self.FPS)
                eventos = pygame.event.get()
                for evento in eventos:
                    match evento.type:
                        case pygame.QUIT:
                            pygame.quit()
                            sys.exit(0)
                        
                        case pygame.KEYDOWN:
                            match evento.key:
                                case pygame.K_TAB:
                                    cambiar_modo()
                                case pygame.K_ESCAPE:
                                    if self.esPausa:
                                        #self.form_menu.enable_disable(self.esPausa)
                                        self.esPausa = False
                                    else:
                                        #self.form_menu.enable_disable()
                                        self.esPausa = True
                                    
                                    print("Termine")
                if self.esPausa:
                    self.PANTALLA.fill((0, 0, 0))
                    self.form_menu.update(eventos)
                else: 
                    keys = pygame.key.get_pressed() 
                
                    if keys[pygame.K_RIGHT]:
                        self.mi_personaje.que_hace = "derecha"
                        self.mi_personaje.direccion = "derecha"
                    elif keys[pygame.K_LEFT]:
                        self.mi_personaje.que_hace = "izquierda"
                        self.mi_personaje.direccion = "izquierda"
                    elif keys[pygame.K_UP]:
                        self.mi_personaje.que_hace = "salta"
                    elif keys[pygame.K_r]:
                        self.mi_personaje.que_hace = "ataca"
                    elif keys[pygame.K_t]:
                        self.mi_personaje.que_hace = "ataca_distancia"
                    else:
                        self.mi_personaje.que_hace = "quieto"
                    self.tiempo_actual = pygame.time.get_ticks()/1000
                    self.actualizar_pantalla()
                    self.dibujar_cronometro(time.time() - self.time)
                    self.activar_jefe()
                    self.derrota()
                    #self.spawn_grupo.sprites()[0].activar_spawn()
                    for spawn in self.spawn_grupo:
                        spawn.activar_spawn(self.mi_personaje, self.enemigos_grupo)
                        
                    if get_modo():
                        for piso in self.plataformas_grupo:
                            pygame.draw.rect(self.PANTALLA, "Blue",piso.rect,3)
                        for piso in self.trampas_grupo:
                            pygame.draw.rect(self.PANTALLA, "Blue",piso.rect,3)
                        
                        for enemigo in self.enemigos_grupo:
                            pygame.draw.rect(self.PANTALLA,"Blue",enemigo.rect,3)
                        pygame.draw.rect(self.PANTALLA,"Blue", self.mi_personaje.rect,3)
                        for disparos in self.mi_personaje.ataques_distancia_grupo:
                            pygame.draw.rect(self.PANTALLA,"Blue", disparos.rect,3)
                    
                        for spawn in self.spawn_grupo:
                            pygame.draw.rect(self.PANTALLA,"Blue", spawn.rect,3)
                        self.mi_personaje.mostrar_ataque =True
                    else:
                        self.mi_personaje.mostrar_ataque = False
                    if time.time() - self.time > 6000:
                        self.game_over = True
                    
                pygame.display.flip()
            self.form_menu.guardar_puntaje(self.puntaje_final)
        except Exception as e:
            self.ficheros.escribir_excepcion(e)
    
    

            
    def actualizar_pantalla(self):
        """brief: Se encarga de actualizar y dibujar los elementos
        parameters: self
        return:None
        """
        volumen_efectos = self.form_menu.volumen_efectos
        self.PANTALLA.blit(self.fondo, self.fondo_rect)
        self.plataformas_grupo.draw(self.PANTALLA)
        self.trampas_grupo.draw(self.PANTALLA)
        self.PANTALLA.get_width()
        self.item_grupo.draw(self.PANTALLA)
        self.spawn_grupo.draw(self.PANTALLA)
        if self.hay_aliado and self.jefe_activo:
            self.aliado_grupo.update(self.PANTALLA,self.mi_personaje,self.item_grupo)
        #llamamos a update para actualizar sus posiciones
        self.personaje_grupo.update(self.PANTALLA,self.plataformas_grupo,self.trampas_grupo, self.item_grupo,self.enemigos_grupo,volumen_efectos)
        self.enemigos_grupo.update(self.PANTALLA,self.plataformas_grupo,self.mi_personaje, volumen_efectos)

    def dibujar_cronometro(self, tiempo):
        text = self.fuente.render(f"Tiempo: {int(tiempo)}", True, (0, 0, 255))
        self.PANTALLA.blit(text, (30, 45))

        
    def activar_jefe(self):
        """brief:  activa la presencia del jefe en el juego cuando ya no hay enemigos
        parameters: self
        return: none
        """
        if len(self.enemigos_grupo) == 0 and not self.jefe_activo :
            self.enemigos_grupo.add(self.jefe)
            self.jefe_activo = True
        elif len(self.enemigos_grupo) == 0 and self.jefe_activo:
            self.nivel_completado()
            
    def derrota(self):
        
        if self.mi_personaje.animacion_muerto:
            text = self.fuente.render(f"Usted ha muerto",True,(255,0,0))
            self.puntaje_final += self.mi_personaje.puntaje 
            self.PANTALLA.blit(text, (675, 350))
            self.RELOJ.tick(0)
            pygame.display.update()
            pygame.time.delay(5000)
            self.game_over = True
            
    def nivel_completado(self):
        """brief:
        parameters:
        return:
        """
        reproducir_sonido("Recursos/Sonidos/Efectos/nivel_completo.wav",0.5)
        text = self.fuente.render(f"Nivel Completado",True,(255,0,0))
        self.PANTALLA.blit(text, (675, 350))
        self.RELOJ.tick(0)
        self.index += 1
        self.jefe_activo = False
        self.puntaje_final += self.mi_personaje.puntaje 
        pygame.display.update()
        pygame.time.delay(5000)
        self.establecer_nivel(self.index)
                
            
            
if __name__ == "__main__":
    W = 1350
    H = 700
    posicion_inicial = (H/2 - 70, 500)
    tamaño = (75,85)
    
    lista_niveles = []
    
    #region nivel 1
    personaje_grupo = pygame.sprite.Group()
    enemigos_grupo = pygame.sprite.Group()
    plataformas_grupo = pygame.sprite.Group()
    trampas_grupo = pygame.sprite.Group()
    item_grupo = pygame.sprite.Group()
    spawn_grupo = pygame.sprite.Group()
    mi_personaje = Protagonista(tamaño, posicion_inicial,10,10,400)
    personaje_grupo.add(mi_personaje)
            
    enemigos_grupo.add(Enemigo(tamaño, (580,500),5,30,3,"zombie",2,10,300))
    enemigos_grupo.add(Enemigo(tamaño, (100,500),10,10,3,"zombie",2,10,300))    

    #pisos
    mi_piso = ElementoGrafico(0,575,W,20,"plataforma2")
    plataformas_grupo.add(mi_piso)

    plataformas_grupo.add(ElementoGrafico(0,460,100,20,"plataforma2"))
    plataformas_grupo.add(ElementoGrafico(300,350,100,20,"plataforma2"))
    plataformas_grupo.add(ElementoGrafico(0,250,100,20,"plataforma2"))
    plataformas_grupo.add(ElementoGrafico(330,150,100,20,"plataforma2"))
    plataformas_grupo.add(ElementoGrafico(450,100,400,20,"plataforma2"))
    plataformas_grupo.add(ElementoGrafico(650,450,200,20,"plataforma2"))
    plataformas_grupo.add(ElementoGrafico(950,350,200,20,"plataforma2"))
    #trampas
    trampas_grupo.add(ElementoGrafico(450,535,100,50,"trampa"))
    trampas_grupo.add(ElementoGrafico(950,535,100,50,"trampa"))
    #items
    item_grupo.add(Item(380,130,20,20,"vida","item_vida",10))
    item_grupo.add(Item(1000,310,40,40,"magia","item_magia",5))
    item_grupo.add(Item(20,410,30,30,"coin","item_coin",10))
    item_grupo.add(Item(340,310,30,30,"coin","item_coin",10))
    #spawn
    spawn_activo = False
    spawn = Spawn(720,350,60,100,"spawn","zombie",10,1)
    spawn.ajustar_tamanio_rectangulo(200,spawn.rect.height)
    
    spawn_grupo.add(spawn)
    jefe = Enemigo((75, 85), (720, 350), 10, 45, 20,"esqueleto",1,100,300)
    #endregion
    
    
    nivel_1 = Nivel(personaje_grupo,enemigos_grupo,plataformas_grupo, trampas_grupo,
                    item_grupo, spawn_grupo, "Fondo","Sadness",(W,H), jefe)
    lista_niveles.append(nivel_1)
    
    #region nivel 2
    personaje_grupo = pygame.sprite.Group()
    enemigos_grupo = pygame.sprite.Group()
    plataformas_grupo = pygame.sprite.Group()
    trampas_grupo = pygame.sprite.Group()
    item_grupo = pygame.sprite.Group()
    spawn_grupo = pygame.sprite.Group()
    mi_personaje = Protagonista(tamaño, posicion_inicial,10,60,10)
    personaje_grupo.add(mi_personaje)
    
    enemigos_grupo.add(Enemigo(tamaño, (30,500),5,30,3,"zombie",3,10,300))        
    enemigos_grupo.add(Enemigo(tamaño, (1000,500),5,30,3,"esqueleto",3,20,300))
    enemigos_grupo.add(Enemigo(tamaño, (600,100),10,10,3,"esqueleto",3,20,300))    
    enemigos_grupo.add(Enemigo(tamaño, (1000,210),5,10,3,"zombie",3,10,300))
    #pisos
    mi_piso = ElementoGrafico(0,575,W,20,"plataforma3")
    plataformas_grupo.add(mi_piso)

    #plataformas_grupo.add(ElementoGrafico(0,450,100,20,"plataforma2"))
    plataformas_grupo.add(ElementoGrafico(350,350,100,30,"plataforma3"))
    plataformas_grupo.add(ElementoGrafico(50,250,100,30,"plataforma3"))
    plataformas_grupo.add(ElementoGrafico(330,150,100,30,"plataforma3"))
    plataformas_grupo.add(ElementoGrafico(450,100,400,30,"plataforma3"))
    plataformas_grupo.add(ElementoGrafico(650,450,200,30,"plataforma3"))
    plataformas_grupo.add(ElementoGrafico(950,250,200,30,"plataforma3"))
    #trampas
    trampas_grupo.add(ElementoGrafico(20,535,100,50,"trampa"))
    trampas_grupo.add(ElementoGrafico(550,535,100,50,"trampa"))
    #items
    item_grupo.add(Item(650,80,20,20,"vida","item_vida",10))
    item_grupo.add(Item(1000,210,40,40,"magia","item_magia",5))
    item_grupo.add(Item(20,410,30,30,"coin","item_coin",10))
    item_grupo.add(Item(340,310,30,30,"coin","item_coin",10))
    #spawn
    spawn_activo = False
    spawn = Spawn(720,350,60,100,"spawn","esqueleto",20,3)
    spawn.ajustar_tamanio_rectangulo(200,spawn.rect.height)
    
    spawn_grupo.add(spawn)
    jefe = Enemigo((75, 85), (720, 350), 10, 45, 80,"brujo",5,300,150)
    #endregion
    
    nivel2 = Nivel (personaje_grupo,enemigos_grupo,plataformas_grupo, trampas_grupo,
                    item_grupo, spawn_grupo, "Fondo_2","Time",(W,H), jefe)

    lista_niveles.append(nivel2)

   #region nivel 3
    personaje_grupo = pygame.sprite.Group()
    enemigos_grupo = pygame.sprite.Group()
    plataformas_grupo = pygame.sprite.Group()
    trampas_grupo = pygame.sprite.Group()
    item_grupo = pygame.sprite.Group()
    spawn_grupo = pygame.sprite.Group()
    aliado_grupo = pygame.sprite.Group()
    
    mi_personaje = Protagonista(tamaño, posicion_inicial,10,70,30)
    personaje_grupo.add(mi_personaje)
    
    enemigos_grupo.add(Enemigo(tamaño, (1200,500),5,25,20,"zombie",3,10,300)) 
    enemigos_grupo.add(Enemigo(tamaño, (700,500),8,25,20,"zombie",3,10,300))        
    enemigos_grupo.add(Enemigo(tamaño, (150,350),5,5,30,"esqueleto",3,20,300))
    enemigos_grupo.add(Enemigo(tamaño, (1050,230),10,5,30,"esqueleto",3,20,300))    
    
    #enemigos_grupo.add(Enemigo(tamaño, (100,250),5,10,20,"zombie",3,20,300))
    #pisos
    mi_piso = ElementoGrafico(0,575,W,20,"plataforma5")
    plataformas_grupo.add(mi_piso)

    #plataformas_grupo.add(ElementoGrafico(0,450,100,20,"plataforma2"))
    plataformas_grupo.add(ElementoGrafico(400,450,100,20,"plataforma5"))
    plataformas_grupo.add(ElementoGrafico(150,350,100,20,"plataforma5"))
    plataformas_grupo.add(ElementoGrafico(360,250,100,20,"plataforma5"))
    plataformas_grupo.add(ElementoGrafico(700,350,400,20,"plataforma5"))
    plataformas_grupo.add(ElementoGrafico(1000,230,200,20,"plataforma5"))
    plataformas_grupo.add(ElementoGrafico(1200,450,130,20,"plataforma5"))
    plataformas_grupo.add(ElementoGrafico(650,150,200,20,"plataforma5"))
    #trampa
    trampas_grupo.add(ElementoGrafico(480,535,100,50,"trampa"))
    trampas_grupo.add(ElementoGrafico(900,310,100,50,"trampa"))
    #items
    item_grupo.add(Item(450,420,20,20,"vida","item_vida",10))
    item_grupo.add(Item(1050,320,40,40,"magia","item_magia",15))
    item_grupo.add(Item(700,320,30,30,"coin","item_coin",10))
    item_grupo.add(Item(200,310,30,30,"coin","item_coin",10))
    item_grupo.add(Item(1000,545,30,30,"coin","item_coin",10))
    #spawn
    spawn_activo = False
    spawn = Spawn(730,50,60,100,"spawn","brujo",60,4,(650,0))
    spawn.ajustar_tamanio_rectangulo(200,spawn.rect.height)
    spawn_grupo.add(spawn)

    jefe = Enemigo((75, 85), (900, 550), 7, 33, 480,"mago",4,400,300)
    #endregion
    
    nivel_3 = Nivel (personaje_grupo,enemigos_grupo,plataformas_grupo, trampas_grupo,
                    item_grupo, spawn_grupo, "Fondo_3","samirade",(W,H), jefe) 
    lista_niveles.append(nivel_3)




    #region nivel 4
    personaje_grupo = pygame.sprite.Group()
    enemigos_grupo = pygame.sprite.Group()
    plataformas_grupo = pygame.sprite.Group()
    trampas_grupo = pygame.sprite.Group()
    item_grupo = pygame.sprite.Group()
    spawn_grupo = pygame.sprite.Group()
    aliado_grupo = pygame.sprite.Group()
    mi_personaje = Protagonista(tamaño, posicion_inicial,10,60,20)
    personaje_grupo.add(mi_personaje)
    
    enemigos_grupo.add(Enemigo(tamaño, (1200,500),5,10,20,"zombie",3,10,300))        
    enemigos_grupo.add(Enemigo(tamaño, (1000,570),5,15,30,"esqueleto",3,20,300))
    enemigos_grupo.add(Enemigo(tamaño, (650,100),10,10,30,"esqueleto",3,20,300))    
    enemigos_grupo.add(Enemigo(tamaño, (700,410),5,10,20,"zombie",3,20,300))
    enemigos_grupo.add(Enemigo(tamaño, (100,250),5,10,20,"zombie",3,20,300))
    #pisos
    mi_piso = ElementoGrafico(0,575,W,20,"plataforma4")
    plataformas_grupo.add(mi_piso)

    #plataformas_grupo.add(ElementoGrafico(0,450,100,20,"plataforma2"))
    plataformas_grupo.add(ElementoGrafico(300,350,100,20,"plataforma4"))
    plataformas_grupo.add(ElementoGrafico(100,250,100,20,"plataforma4"))
    plataformas_grupo.add(ElementoGrafico(330,150,100,20,"plataforma4"))
    plataformas_grupo.add(ElementoGrafico(450,100,400,20,"plataforma4"))
    plataformas_grupo.add(ElementoGrafico(550,450,200,20,"plataforma4"))
    plataformas_grupo.add(ElementoGrafico(600,250,130,20,"plataforma4"))
    plataformas_grupo.add(ElementoGrafico(1000,335,150,20,"plataforma4"))
    #trampa
    trampas_grupo.add(ElementoGrafico(20,535,100,50,"trampa"))
    trampas_grupo.add(ElementoGrafico(550,535,100,50,"trampa"))
    #items
    item_grupo.add(Item(650,80,20,20,"vida","item_vida",10))
    item_grupo.add(Item(600,210,40,40,"magia","item_magia",5))
    item_grupo.add(Item(1050,300,40,40,"magia","item_magia",5))
    item_grupo.add(Item(700,410,30,30,"coin","item_coin",10))
    item_grupo.add(Item(340,310,30,30,"coin","item_coin",10))
    item_grupo.add(Item(650,420,20,20,"vida","item_vida",10))
    item_grupo.add(Item(1200,545,30,30,"coin","item_coin",10))
    #spawn
    spawn_activo = False
    spawn = Spawn(650,0,60,100,"spawn","esqueleto",20,2,(650,0))
    spawn.ajustar_tamanio_rectangulo(200,spawn.rect.height)
    spawn_grupo.add(spawn)
    aliado = Aliado(280,495)
    aliado_grupo.add(aliado)
    jefe = Enemigo((75, 85), (900, 550), 7, 33, 480,"mago_oscuro",4,1000,300)
    #endregion
    
    nivel_4 = Nivel (personaje_grupo,enemigos_grupo,plataformas_grupo, trampas_grupo,
                    item_grupo, spawn_grupo, "Fondo_4","No_Time_For_Caution",(W,H), jefe,aliado_grupo,True) 
    lista_niveles.append(nivel_4)
    
    
    game = Game(lista_niveles,W,H)
    game.RunGame()