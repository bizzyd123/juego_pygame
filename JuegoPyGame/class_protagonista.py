from class_personaje import *
from configuraciones import girar_imagenes, reproducir_sonido
from class_ataque_distancia import *
class Protagonista(Personaje):
    def __init__(self, tamaño, posicion_inicial, velocidad,vida,daño):
        animaciones = self.crear_animaciones()
        Personaje.__init__(self,tamaño, animaciones, posicion_inicial, velocidad,vida,daño)
        self.puntaje = 0
        self.tiempo_ultimo_ataque = 0
        self.magia_total = 5
        self.vivo = True
        self.animacion_muerto = False
        
    def crear_animaciones(self)-> dict:
        personaje_quieto = [pygame.image.load("Recursos/Personaje/Quieto/1.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/2.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/3.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/4.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/5.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/6.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/7.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/8.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/9.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/10.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/11.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/12.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/13.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/14.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/15.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/16.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/17.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/18.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/19.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/20.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/21.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/22.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/23.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/24.png"),
                    pygame.image.load("Recursos/Personaje/Quieto/25.png"),
                    ]

        personaje_camina = [#pygame.image.load("Recursos/Personaje/Camina/1.png"),
                            #pygame.image.load("Recursos/Personaje/Camina/2.png"),
                            pygame.image.load("Recursos/Personaje/Camina/3.png"),
                            pygame.image.load("Recursos/Personaje/Camina/4.png"),
                            pygame.image.load("Recursos/Personaje/Camina/5.png"),
                            pygame.image.load("Recursos/Personaje/Camina/6.png"),
                            pygame.image.load("Recursos/Personaje/Camina/7.png"),
                            pygame.image.load("Recursos/Personaje/Camina/8.png"),
                            #pygame.image.load("Recursos/Personaje/Camina/9.png")
                            ]

        personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)
        personaje_salta_derecha = [pygame.image.load("Recursos/Personaje/Salta/2.png"),
                        pygame.image.load("Recursos/Personaje/Salta/2.png"),
                        pygame.image.load("Recursos/Personaje/Salta/3.png"),
                        pygame.image.load("Recursos/Personaje/Salta/4.png"),
                        pygame.image.load("Recursos/Personaje/Salta/5.png"),                   
                        ]
        personaje_salta_izquierda = girar_imagenes(personaje_salta_derecha,True,False)
        personaje_ataca_derecha = [ pygame.image.load("Recursos/Personaje/Ataca/1.png"),
                            pygame.image.load("Recursos/Personaje/Ataca/2.png"),
                            pygame.image.load("Recursos/Personaje/Ataca/3.png"),
                            pygame.image.load("Recursos/Personaje/Ataca/4.png"),
                            pygame.image.load("Recursos/Personaje/Ataca/5.png"),
                            pygame.image.load("Recursos/Personaje/Ataca/6.png"),
                            pygame.image.load("Recursos/Personaje/Ataca/7.png"),
                            pygame.image.load("Recursos/Personaje/Ataca/8.png"),
                            pygame.image.load("Recursos/Personaje/Ataca/9.png"),
                            pygame.image.load("Recursos/Personaje/Ataca/10.png"),
                            pygame.image.load("Recursos/Personaje/Ataca/11.png"),
                            pygame.image.load("Recursos/Personaje/Ataca/12.png")
        ]
        personaje_ataca_izquierda = girar_imagenes(personaje_ataca_derecha,True,False)
        
        personaje_ataca_distancia_derecha = [
            pygame.image.load("Recursos/Personaje/Distancia/1.png"),
            pygame.image.load("Recursos/Personaje/Distancia/2.png"),
            pygame.image.load("Recursos/Personaje/Distancia/3.png"),
            pygame.image.load("Recursos/Personaje/Distancia/4.png")
        ]
        personaje_muere_derecha = [
            pygame.image.load("Recursos/Personaje/Muere/1.png"),
            pygame.image.load("Recursos/Personaje/Muere/2.png"),
            pygame.image.load("Recursos/Personaje/Muere/3.png"),
            pygame.image.load("Recursos/Personaje/Muere/4.png"),
            pygame.image.load("Recursos/Personaje/Muere/5.png"),
            pygame.image.load("Recursos/Personaje/Muere/6.png"),
            pygame.image.load("Recursos/Personaje/Muere/7.png"),
            pygame.image.load("Recursos/Personaje/Muere/8.png"),
            pygame.image.load("Recursos/Personaje/Muere/9.png"),
        ]
        personaje_muere_izquierda = girar_imagenes(personaje_muere_derecha,True,False)
        personaje_ataca_distancia_izquierda = girar_imagenes(personaje_ataca_distancia_derecha,True,False)
        
        personaje_muerto_derecha = [pygame.image.load("Recursos/Personaje/Muere/muerto.png")]
        personaje_muerto_izquierda = girar_imagenes(personaje_muerto_derecha,True,False)
        
        diccionario_animaciones = {}
        diccionario_animaciones["quieto"] = personaje_quieto
        diccionario_animaciones["salta_derecha"] = personaje_salta_derecha
        diccionario_animaciones["salta"] = personaje_salta_derecha
        diccionario_animaciones["salta_izquierda"] = personaje_salta_izquierda
        diccionario_animaciones["camina_derecha"] = personaje_camina
        diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda 
        diccionario_animaciones["ataca_derecha"] = personaje_ataca_derecha
        diccionario_animaciones["ataca_izquierda"] = personaje_ataca_izquierda
        diccionario_animaciones["ataca_distancia_derecha"] = personaje_ataca_distancia_derecha
        diccionario_animaciones["ataca_distancia_izquierda"] = personaje_ataca_distancia_izquierda
        diccionario_animaciones["personaje_muere_izquierda"] = personaje_muere_izquierda
        diccionario_animaciones["personaje_muere_derecha"] = personaje_muere_derecha
        diccionario_animaciones["personaje_muerto_derecha"] = personaje_muerto_derecha
        diccionario_animaciones["personaje_muerto_izquierda"] = personaje_muerto_izquierda
        return diccionario_animaciones

    def estoy_vivo(self, enemigos_grupo:list):
        """brief: verifico que el personaje este con vida, en caso positivo
        se analizan los ataques, en caso negativo se ejecuta la animacion de muerte
        parameters:enemigos_grupo
        return:None
        """
        if self.vida <= 0:
            self.que_hace ="morir"
            if self.direccion == "derecha" and len(self.animaciones["personaje_muerto_derecha"]) == self.contador_pasos:
                self.animacion_muerto = True
            elif  self.direccion == "izquierda" and len(self.animaciones["personaje_muerto_izquierda"]) == self.contador_pasos:
                self.animacion_muerto = True
            if self.animacion_muerto:
                self.que_hace = "muerto" 
        else:
            for enemigo in enemigos_grupo:
                self.verificar_me_pegan(enemigo)
                resultado = self.verificar_ataques_melee(enemigo)
                if resultado:
                    enemigos_grupo.remove(enemigo)
                    reproducir_sonido("Recursos/Sonidos/Efectos/muerte_enemigo.wav",self.volumen_efectos)
                    break
                resultado = self.verificar_ataque_distancia(enemigo)
                if resultado:
                    enemigos_grupo.remove(enemigo)
                    reproducir_sonido("Recursos/Sonidos/Efectos/muerte_enemigo.wav",self.volumen_efectos)
                    break
                
                
                
    def verificar_ataques_melee(self,enemigo):
        """brief: verifica si el rectangulo de ataque del personaje colisiona con el enemigo
        parameters:enemigos_grupo
        return: bool
        """
        eliminar = False
        if self.rect_ataque.colliderect(enemigo.rect) and self.rect_ataque.width > 0:
            # Se detectó una colisión entre el rectángulo de ataque y el enemigo
            enemigo.vida -= 1
            # También puedes realizar otras acciones, como eliminar el enemigo si su vida llega a cero
            if enemigo.vida <= 0:
                #marco el enemigo para borrar
                eliminar = True
                self.puntaje += enemigo.valor_puntaje
        return eliminar
                    
    def verificar_me_pegan(self,enemigo):
        """"brief: verifica si hay colision, de ser asi ataca 
        y se llama a la funcion de reproducir sonido para el efecto de ataque
        parameters:self, enemigo
        return: None
        """
        if self.rect.colliderect(enemigo.rect):
            enemigo.que_hace = "ataca"
            self.vida -= enemigo.daño
            reproducir_sonido("Recursos/Sonidos/Efectos/player-damage.wav",self.volumen_efectos)
            self.colisiones_laterales([enemigo])
                
    def verificar_ataque_distancia(self, enemigo):
        """brief: verifica si el disparo de ataque del personaje colisiona con el enemigo
        parameters:enemigos_grupo
        return: bool
        """
        eliminar= False
        for disparo in self.ataques_distancia_grupo:
                if disparo.rect.colliderect(enemigo.rect) :
                    enemigo.vida -= self.daño*2
                    if enemigo.vida <= 0:
                        #marco el enemigo para borrar
                        eliminar = True
                        self.puntaje += enemigo.valor_puntaje
                    self.ataques_distancia_grupo.remove(disparo)
        return eliminar
                        
    def update(self, pantalla,mis_pisos,lista_trampas, lista_items,enemigos_grupo, volumen_efectos):
        """brief: el metodo se encarga de hacer las animaciones del protagonista, ademas de inicar
        los eventos de ataque y las colisiones de dichos ataques
        parameters:
        return:
        """
        salto = "salta_derecha"
        self.volumen_efectos = volumen_efectos
        self.validar_ubicacion_y()
        clave = pygame.key.get_pressed()
        self.estoy_vivo(enemigos_grupo)
        
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                if clave[pygame.K_UP]:
                    salto = "salta_derecha"
                self.mover(self.velocidad,pantalla)
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                clave = pygame.key.get_pressed()
                if clave[pygame.K_UP]:
                    salto = "salta_izquierda"
                self.mover(self.velocidad * -1,pantalla)
            case "salta":
                if not self.esta_saltando:
                    reproducir_sonido("Recursos/Sonidos/Efectos/jump.wav",self.volumen_efectos)
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "quieto":
                if not self.esta_saltando:
                    self.animar(pantalla, "quieto")
            case "morir":
                self.gravedad = 0
                self.desplazamiento_y =0
                self.velocidad = 0
                self.esta_saltando = False
                if self.direccion == "derecha":
                    self.animar(pantalla,"personaje_muere_derecha")
                else:
                    self.animar(pantalla,"personaje_muere_izquierda")
            case "muerto":
                reproducir_sonido("Recursos/Sonidos/Efectos/personaje_muerto.wav",self.volumen_efectos)
                self.gravedad = 0
                self.desplazamiento_y =0
                self.velocidad = 0
                self.esta_saltando = False
                if self.direccion == "derecha":
                    self.animar(pantalla,"personaje_muerto_derecha")
                else:
                    self.animar(pantalla,"personaje_muerto_izquierda")
            case "ataca":
                    reproducir_sonido("Recursos/Sonidos/Efectos/espada.wav",self.volumen_efectos)
                    if self.direccion == "izquierda" :
                        self.animar(pantalla,"ataca_izquierda")
                    else : 
                        self.animar(pantalla,"ataca_derecha")
                    if self.mostrar_ataque:
                        pygame.draw.rect(pantalla, (255, 0, 0), self.rect_ataque)  # Dibuja el rectángulo de ataque en rojo
            case "ataca_distancia":
                tiempo_actual = pygame.time.get_ticks()
                if tiempo_actual - self.tiempo_ultimo_ataque >= 500 and self.magia_total > 0:
                    self.magia_total -= 1
                    reproducir_sonido("Recursos/Sonidos/Efectos/disparo_protagonista.wav",self.volumen_efectos)
                    self.tiempo_ultimo_ataque = tiempo_actual
                    if self.direccion == "izquierda":
                        self.animar(pantalla,"ataca_izquierda")
                    elif self.direccion == "derecha":
                        self.animar(pantalla,"ataca_derecha")
                    self.actualizar_ataque_distancia()
                else:
                    self.animar(pantalla,"quieto")
        self.actualizar_rect_ataque()
        self.colision_items(lista_items)
        self.aplicar_gravedad(pantalla, mis_pisos,salto)
        self.colision_trampas(lista_trampas)
        self.renderizar_vida(pantalla,"Red")
        self.dibujar_informacion(pantalla)
        self.eliminar_disparo(pantalla)
        self.ataques_distancia_grupo.update(pantalla)
        
    def colision_items(self, lista_items):
        """brief:verifica si hay colision entre el protagonista y los items,
        de ser asi se incrementa vida, magia y puntaje
        parameters: lista_items
        return
        """
        for item in lista_items:
            if item.rect.colliderect(self.rect):
                match item.tipo:
                    case "item_vida":
                        self.vida += item.efecto
                        reproducir_sonido("Recursos/Sonidos/Efectos/vida.wav",self.volumen_efectos)
                    case "item_magia":
                        self.magia_total+= item.efecto
                        reproducir_sonido("Recursos/Sonidos/Efectos/pocion.wav",self.volumen_efectos)
                    case "item_coin":
                        self.puntaje += item.efecto
                        reproducir_sonido("Recursos/Sonidos/Efectos/moneda.wav",self.volumen_efectos)
                lista_items.remove(item)
                        
        
    def dibujar_informacion(self, pantalla):
        """brief: renderiza  el puntaje y magia dibujandolo en la pantalla con blit
        parameters: self, pantalla
        return: None
        """
        fuente = pygame.font.Font("Recursos/Fuente/fuente.ttf", 28)
        puntuacion = fuente.render(f"Puntaje:{self.puntaje}", True, (0, 0, 255))
        pantalla.blit(puntuacion, (30,20))
        magia = fuente.render(f"Magia disponible:{self.magia_total}", True, (0, 0, 255))
        pantalla.blit(magia, (30,70))

               
            
    def colision_trampas(self,lista_trampas):
        colisiones = pygame.sprite.spritecollide(self, lista_trampas, False)
        for colision in colisiones:
            if self.rect.bottom >= colision.rect.top-10 and self.rect.bottom - self.limite_velocidad_caida < colision.rect.top:
                self.rect.bottom = colision.rect.top
                self.esta_saltando = False
                self.desplazamiento_y = 0
                self.vida += -self.volumen_efectos
                break
            else:
                if self.rect.right >= colision.rect.left-7 and self.direccion == "derecha" :
                    self.rect.right = colision.rect.left - 2
                elif self.rect.left <= colision.rect.right and self.direccion == "izquierda":
                    self.rect.left = colision.rect.right +2
        
    def actualizar_rect_ataque(self):
        if(self.que_hace == "ataca"):
            if self.direccion == "derecha":
                self.rect_ataque.width = self.rect.width
                self.rect_ataque.height = self.rect.height + 5
                self.rect_ataque.x = self.rect.centerx
                self.rect_ataque.y = self.rect.y
            elif self.direccion == "izquierda":
                self.rect_ataque.width = self.rect.width
                self.rect_ataque.height = self.rect.height + 5
                self.rect_ataque.x = self.rect.left -40
                self.rect_ataque.y = self.rect.y
        else:
            self.rect_ataque.width = 0
            self.rect_ataque.height = 0
            self.rect_ataque.x = 0
            self.rect_ataque.y = 0
            
    def actualizar_ataque_distancia(self):
        if self.que_hace == "ataca_distancia":
            if(self.direccion == "izquierda"):
                ataque = AtaqueDistancia(self.rect.left-40,self.rect.y,10,self.direccion,"prota")
                self.ataques_distancia_grupo.add(ataque)
            else:
                #ataqueDistancia(x,y,velocidad,direccion)
                ataque = AtaqueDistancia(self.rect.right,self.rect.y,10,self.direccion,"prota")
                self.ataques_distancia_grupo.add(ataque)
        else:
            self.rect_ataque.width = 0
            self.rect_ataque.height = 0
            self.rect_ataque.x = 0
            self.rect_ataque.y = 0
