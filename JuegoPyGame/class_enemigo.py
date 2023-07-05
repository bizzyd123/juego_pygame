from class_personaje import *
from class_ataque_distancia import * 
from configuraciones import girar_imagenes, reproducir_sonido
class Enemigo(Personaje):
    def __init__(self, tamaño, posicion_inicial, velocidad, pasos, vida,tipo,daño, valor_puntaje, frecuencia_disparo):
        self.tipo = tipo
        animaciones = self.__crear_animaciones()
        Personaje.__init__(self,tamaño, animaciones, posicion_inicial, velocidad, vida,daño)
        self.pasos = pasos
        #animaciones
        self.contador_pasos = 0
        self.pasos_movimiento = 0
        self.valor_puntaje = valor_puntaje
        self.frecuencia_disparo = frecuencia_disparo
        self.disparo_potente = 0
    #region  zombie
    def __animacion_zombie(self):
        zombie_camina = [
            pygame.image.load("Recursos/Zombie/Camina/1.png"),
            pygame.image.load("Recursos/Zombie/Camina/2.png"),
            pygame.image.load("Recursos/Zombie/Camina/3.png"),
            pygame.image.load("Recursos/Zombie/Camina/4.png"),
            pygame.image.load("Recursos/Zombie/Camina/5.png"),
            pygame.image.load("Recursos/Zombie/Camina/6.png")
        ]
        zombie_salta = [
            pygame.image.load("Recursos/Zombie/Camina/1.png")
            
        ]
        zombie_quieto = [
            pygame.image.load("Recursos/Zombie/Camina/1.png")
        ]
        zombie_ataca = [
                pygame.image.load("Recursos/Zombie/Ataque/1.png"),
                pygame.image.load("Recursos/Zombie/Ataque/2.png"),
                pygame.image.load("Recursos/Zombie/Ataque/3.png"),
                pygame.image.load("Recursos/Zombie/Ataque/4.png")
        ]
        zombie_camina_izquierda  = girar_imagenes(zombie_camina,True,False)
        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["quieto"] = zombie_quieto
        diccionario_animaciones_enemigo["salta"] = zombie_salta
        diccionario_animaciones_enemigo["camina_derecha"] = zombie_camina_izquierda 
        diccionario_animaciones_enemigo["camina_izquierda"] = zombie_camina             #pasos
        diccionario_animaciones_enemigo["ataca"] = zombie_ataca 
        return diccionario_animaciones_enemigo
    #endregion
    
    #region  esqueleto
    def __animacion_esqueleto(self):
        esqueleto_camina = [
            pygame.image.load("Recursos/Esqueleto/Camina/1.png"),
            pygame.image.load("Recursos/Esqueleto/Camina/2.png"),
            pygame.image.load("Recursos/Esqueleto/Camina/3.png"),
            pygame.image.load("Recursos/Esqueleto/Camina/4.png"),
        ]
        esqueleto_salta = [
            pygame.image.load("Recursos/esqueleto/Camina/1.png")
            
        ]
        esqueleto_quieto = [
            pygame.image.load("Recursos/esqueleto/Camina/1.png")
        ]
        esqueleto_ataca = [
                pygame.image.load("Recursos/esqueleto/Ataque/1.png"),
                pygame.image.load("Recursos/esqueleto/Ataque/2.png"),
        ]
        esqueleto_camina_izquierda  = girar_imagenes(esqueleto_camina,True,False)
        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["quieto"] = esqueleto_quieto
        diccionario_animaciones_enemigo["salta"] = esqueleto_salta
        diccionario_animaciones_enemigo["camina_derecha"] = esqueleto_camina_izquierda 
        diccionario_animaciones_enemigo["camina_izquierda"] = esqueleto_camina             #pasos
        diccionario_animaciones_enemigo["ataca"] = esqueleto_ataca 
        return diccionario_animaciones_enemigo
    #endregion
    
    #region  Brujo
    def __animacion_brujo(self):
        brujo_camina_izquierda = [
            pygame.image.load("Recursos/Brujo/Camina/1.png"),
            pygame.image.load("Recursos/Brujo/Camina/2.png"),
            pygame.image.load("Recursos/Brujo/Camina/3.png"),
            pygame.image.load("Recursos/Brujo/Camina/4.png"),
        ]
        brujo_salta = [
            pygame.image.load("Recursos/Brujo/Camina/1.png")
            
        ]
        brujo_quieto = [
            pygame.image.load("Recursos/Brujo/Camina/1.png")
        ]
        brujo_ataca = [
                pygame.image.load("Recursos/Brujo/Ataque/1.png"),
                pygame.image.load("Recursos/Brujo/Ataque/2.png"),
                pygame.image.load("Recursos/Brujo/Ataque/3.png"),
        ]
        brujo_camina_derecha  = girar_imagenes(brujo_camina_izquierda,True,False)
        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["quieto"] = brujo_quieto
        diccionario_animaciones_enemigo["salta"] = brujo_salta
        diccionario_animaciones_enemigo["camina_derecha"] = brujo_camina_izquierda 
        diccionario_animaciones_enemigo["camina_izquierda"] = brujo_camina_derecha             #pasos
        diccionario_animaciones_enemigo["ataca"] = brujo_ataca 
        return diccionario_animaciones_enemigo
    #endregion
    
    #region  Mago
    def __animacion_mago(self):
        mago_camina = [
            pygame.image.load("Recursos/Mago/Camina/1.png"),
            pygame.image.load("Recursos/Mago/Camina/2.png"),
            pygame.image.load("Recursos/Mago/Camina/3.png"),
            pygame.image.load("Recursos/Mago/Camina/4.png"),
        ]
        mago_salta = [
            pygame.image.load("Recursos/Mago/Camina/1.png")
            
        ]
        mago_quieto = [
            pygame.image.load("Recursos/Mago/Camina/1.png")
        ]
        mago_ataca = [
                pygame.image.load("Recursos/Mago/Camina/1.png"),
                pygame.image.load("Recursos/Mago/Camina/2.png"),
                pygame.image.load("Recursos/Mago/Camina/3.png"),
        ]
        mago_camina_izquierda  = girar_imagenes(mago_camina,True,False)
        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["quieto"] = mago_quieto
        diccionario_animaciones_enemigo["salta"] = mago_salta
        diccionario_animaciones_enemigo["camina_derecha"] = mago_camina 
        diccionario_animaciones_enemigo["camina_izquierda"] = mago_camina_izquierda             #pasos
        diccionario_animaciones_enemigo["ataca"] = mago_ataca 
        return diccionario_animaciones_enemigo
    def __animacion_mago_oscuro(self):
        mago_camina = [
            pygame.image.load("Recursos/Mago_Oscuro/Camina/1.png"),
            pygame.image.load("Recursos/Mago_Oscuro/Camina/2.png"),
            pygame.image.load("Recursos/Mago_Oscuro/Camina/3.png"),
            pygame.image.load("Recursos/Mago_Oscuro/Camina/4.png"),
        ]
        mago_salta = [
            pygame.image.load("Recursos/Mago_Oscuro/Camina/1.png")

        ]
        mago_quieto = [
            pygame.image.load("Recursos/Mago_Oscuro/Camina/1.png")
        ]
        mago_ataca = [
                pygame.image.load("Recursos/Mago_Oscuro/Camina/1.png"),
                pygame.image.load("Recursos/Mago_Oscuro/Camina/2.png"),
                pygame.image.load("Recursos/Mago_Oscuro/Camina/3.png"),
        ]
        mago_camina_izquierda  = girar_imagenes(mago_camina,True,False)
        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["quieto"] = mago_quieto
        diccionario_animaciones_enemigo["salta"] = mago_salta
        diccionario_animaciones_enemigo["camina_derecha"] = mago_camina 
        diccionario_animaciones_enemigo["camina_izquierda"] = mago_camina_izquierda             #pasos
        diccionario_animaciones_enemigo["ataca"] = mago_ataca 
        return diccionario_animaciones_enemigo
    #endregion
    def __crear_animaciones(self):
        match self.tipo:
            case    "mago_oscuro":
                animaciones = self.__animacion_mago_oscuro()
            case    "zombie":
                animaciones = self.__animacion_zombie()
            case    "esqueleto":
                animaciones = self.__animacion_esqueleto()
            case    "mago":
                animaciones = self.__animacion_mago()
            case    "brujo":
                animaciones = self.__animacion_brujo()
        return animaciones
        
    
    def update(self, pantalla,mis_pisos, personaje, volumen_efectos):
        self.volumen_efectos = volumen_efectos
        
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha") 
                self.mover(self.velocidad,pantalla)
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                self.mover(self.velocidad * -1,pantalla)
            case "ataca":
                self.animar(pantalla,"ataca")
                #self.actualizar_rect_ataque()
        self.mover_solo()
        self.ataca_solo()
        self.ataques_distancia_grupo.update(pantalla)
        self.aplicar_gravedad(pantalla, mis_pisos,"salta")
        self.renderizar_vida(pantalla,"Blue")
        self.colision_disparo(personaje)
        self.eliminar_disparo(pantalla)
        
    def colision_disparo(self, personaje ):
        for disparo in self.ataques_distancia_grupo:
            if disparo.rect.colliderect(personaje.rect) and personaje.vida > 0:
               personaje.vida -= self.daño
               self.ataques_distancia_grupo.remove(disparo)
    
    def mover_solo(self):

        if(self.pasos_movimiento < self.pasos ):
            self.que_hace = "izquierda"
        else:
            self.que_hace = "derecha"
        self.pasos_movimiento +=1
        if(self.pasos_movimiento == self.pasos*2):
            self.pasos_movimiento = 0
            
            
    def ataca_solo(self):
        if(self.tipo != "zombie"):
            tiempo_actual = pygame.time.get_ticks()
            if self.disparo_potente < 3:
                if tiempo_actual - self.tiempo_ultimo_ataque >= self.frecuencia_disparo*10 :
                #if tiempo_actual - self.tiempo_ultimo_ataque >= self.pasos*200 :
                    self.tiempo_ultimo_ataque = tiempo_actual
                    self.disparar(self.que_hace)
                    self.disparo_potente += 1
            elif self.disparo_potente >= 3 and self.disparo_potente < 5:
                if tiempo_actual - self.tiempo_ultimo_ataque >= self.frecuencia_disparo *2 :
                #if tiempo_actual - self.tiempo_ultimo_ataque >= self.pasos*200 :
                    self.tiempo_ultimo_ataque = tiempo_actual
                    self.disparar(self.que_hace)
                    self.disparo_potente += 1
            elif self.disparo_potente == 5 and self.tipo== "brujo" or self.tipo=="mago":
                if tiempo_actual - self.tiempo_ultimo_ataque >= self.frecuencia_disparo*10 :
                #if tiempo_actual - self.tiempo_ultimo_ataque >= self.pasos*200 :
                    self.tiempo_ultimo_ataque = tiempo_actual
                    self.disparar("derecha")
                    self.disparar("izquierda")
                    self.disparo_potente= 0
            else: 
                self.disparo_potente = 0 
            
                
            
    def disparar(self, direccion):
        match self.tipo:
            case "brujo":
                reproducir_sonido("Recursos/Sonidos/Efectos/disparo_brujo.wav",self.volumen_efectos)
            case "mago":
                reproducir_sonido("Recursos/Sonidos/Efectos/disparo_mago.wav",self.volumen_efectos)
            case "esqueleto":
                reproducir_sonido("Recursos/Sonidos/Efectos/disparo_flecha.wav",self.volumen_efectos)
            case "mago_oscuro":
                reproducir_sonido("Recursos/Sonidos/Efectos/disparo_mago.wav",self.volumen_efectos)
        ataque = AtaqueDistancia(self.rect.left-40,self.rect.y,self.velocidad*1.5,direccion,self.tipo)
        self.que_hace = "ataca"
        self.ataques_distancia_grupo.add(ataque)