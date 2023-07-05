from configuraciones import reescalar_imagenes
import pygame
class Personaje(pygame.sprite.Sprite):
    def __init__(self, tamaño: tuple, animaciones: dict, posicion_inicial: tuple, velocidad: int, vida: int, daño:int):
        super().__init__() # Llama al constructor de la clase padre
        self.volumen_efectos= 0.1
        
        #vida
        self.vida = vida # se usa para dibujar la barra de vida
        #ataque
        self.daño = daño
        self.mostrar_ataque = False # se usa para mostrar el cuadrado de ataque
        self.rect_ataque = pygame.Rect(0, 0, 5, 10) # crea el cuadrado de area de ataque
        # Configuración
        self.gravedad = 1 #velocidad de caida
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        self.direccion = "derecha"
        self.desplazamiento_x = 0
        # Animaciones
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones(tamaño[0],tamaño[1])
        #establece el punto de aparicion del personaje
        self.image = self.animaciones[self.que_hace][0]
        self.rect = self.image.get_rect()
        self.rect.x = posicion_inicial[0] # (5,8)
        self.rect.y = posicion_inicial[1]
        
        self.ataques_distancia_grupo = pygame.sprite.Group()
        self.tiempo_ultimo_ataque = 0
    def reescalar_animaciones(self,ancho:int ,alto:int):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (ancho, alto))

    def renderizar_vida(self, pantalla,color):
        """brief: dibuja una barra de vida en la pantalla
        parameters: pantalla, color
        return: None
        """
        # Calcula el ancho de la barra de vida en base al contador de vidas
        largo_vida = self.vida * 2  # Cada vida se representa con un rectángulo de largo 2
        # Dibuja la barra de vida en la pantalla
        pygame.draw.rect(pantalla, color, (self.rect.x, self.rect.y - 10, largo_vida, 8))

    
            
    #que_animacion puede ser "camina_derecha", "camina_izquierda",etc
    def animar(self, pantalla: pygame.surface, que_animacion:str):
        """brief:
        parameters:
        return:
        """
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(animacion[self.contador_pasos], self.rect)
        self.contador_pasos += 1

    def validar_ubicacion_x(self, pantalla:pygame.surface):
        """brief:valida que el personaje siga dentro del limite de la pantalla,
        de ser necesario lo vuelve a establecer dentro de los limites del mapa
        parameters:pantalla
        return: None
        """
        if self.rect.x <= 0:
            self.rect.x = 1
        #pantalla.get_width() me da el largo de la pantalla
        elif self.rect.x >= pantalla.get_width():
            self.rect.x = pantalla.get_width()-30
    
    def validar_ubicacion_y(self):
        if self.rect.y > 700 :
            self.rect.y = 280
            print("la tarea fallo con exito")
    
    def mover(self, velocidad:int, pantalla:pygame.surface):
        """brief:incrementa la posicion en x
        parameters:velocidad, pantalla
        return: None
        """
        self.validar_ubicacion_y()
        self.validar_ubicacion_x(pantalla)
        self.rect.x += velocidad
        
    def colisiones_laterales(self, mis_pisos):
        """brief: se valida que el personaje no pueda atravesar los pisos desde los laterales.
        parameters:mis_pisos
        return: None
        """
        colisiones = pygame.sprite.spritecollide(self, mis_pisos, False)
        for colision in colisiones:
            #hago una cuenta para calcular el margen de error de la colision
            margen_lateral = self.rect.right - colision.rect.left
            #calculo aproximadamente 20 pixeles de margen para tocar la plataforma
            if margen_lateral>= -10 and margen_lateral <= 10 and self.direccion =="derecha" :
                self.rect.right = colision.rect.left-2   
            #hago una cuenta para calcular el margen de error de la colision    
            margen_lateral = colision.rect.right - self.rect.left
            #calculo aproximadamente 20 pixeles de margen para tocar la plataforma
            if margen_lateral>= -10 and margen_lateral <= 10 and self.direccion =="izquierda":
                self.rect.left = colision.rect.right +2
                
    def validar_colisiones_sin_salto(self, mis_pisos):
        """brief: mientras el personaje esta en caida o parado sobre un piso valida las colisiones con la parte superior de los pisos.
        parameters:mis_pisos
        return: None
        """
        self.rect.y += self.desplazamiento_y
        self.colisiones_laterales(mis_pisos)
        for pisos in mis_pisos:
            if self.rect.colliderect(pisos.rect) :
                if self.rect.bottom  > pisos.rect.top:
                    self.esta_saltando = False
                    self.rect.bottom = pisos.rect.top
                    self.desplazamiento_y = 0
                    break
            else:
                self.esta_saltando = True
                
    def validar_colisiones_con_salto(self, mis_pisos):
        """brief: mientras esta saltando valida la colision con los pisos desde arriba o abajo
        parameters:mis_pisos
        return: None
        """
        colisiones = pygame.sprite.spritecollide(self, mis_pisos, False)
        for plataforma in colisiones:
            #hago una cuenta para calcular el margen de error de la colision
            margen_vertical =  self.rect.bottom - plataforma.rect.top
            #calculo aproximadamente 40 pixeles de margen para tocar la plataforma
            if margen_vertical >= -20 and margen_vertical <= 20 and self.desplazamiento_y > 0:
                # Colisión desde arriba 
                self.rect.bottom = plataforma.rect.top
                self.esta_saltando = False
                self.desplazamiento_y = 0

            if self.desplazamiento_y < 0:
                # Colisión desde abajo
                #hago una cuenta para calcular el margen de error de la colision
                margen =  self.rect.top - plataforma.rect.bottom
                #calculo aproximadamente 40 pixeles de margen para tocar la plataforma
                if(self.rect.top< plataforma.rect.bottom and margen >= -20 and margen <= 20):
                    self.rect.top = plataforma.rect.bottom
                    #self.esta_saltando = False
                    self.desplazamiento_y = self.gravedad
        self.colisiones_laterales(mis_pisos)
                
    def aplicar_gravedad(self, pantalla, mis_pisos,salto):
        """brief: se aplica gravedad al personaje para que inicie su caida cuando sea necesario.
        parameters:pantalla, mis_pisos, salto
        return: None
        """
        if not self.esta_saltando:
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
            # Verificar si el rectángulo inferior del personaje está en contacto con algún piso
            self.validar_colisiones_sin_salto(mis_pisos)
        else:
            self.animar(pantalla,salto)
            self.rect.y += self.desplazamiento_y
            self.desplazamiento_y += self.gravedad
            self.validar_colisiones_con_salto(mis_pisos)
            

    def eliminar_disparo(self,pantalla)-> None:
        """brief: se calcula cuando el disparo supero el limite de la pantalla por ambos extremos y elimina el disparo en caso de superarlo 
        parameters: pantalla de tipo surface
        returns: None
        """
        width = pantalla.get_width()
        for disparo in self.ataques_distancia_grupo:
            if disparo.rect.x >= width or disparo.rect.x < 0 :
                #disparos= len(self.ataques_distancia_grupo)
                #print(f"antes de borrar:{disparos}")
                self.ataques_distancia_grupo.remove(disparo)
                #disparos= len(self.ataques_distancia_grupo)
                #print(f"despues de borrar:{disparos}")