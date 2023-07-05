import pygame
from pygame.locals import * 
from form.GUI_form import *
from form.GUI_label import *
from form.GUI_button_image import *
 
 
class FromMenuNiveles(Form):
    def __init__(self,screen,x,y,w,h,nivel, color_background, color_border, active, path_image, score, margen_y, margen_x,  espacio):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self.nivel = nivel
        self._slave = aux_image
        self._score = score
        self._marge_x = margen_y      
        
        self.btn_home = Button_Image(screen= self._slave,
                                     x= w-70,
                                     y = h-70,
                                     master_x= x,
                                     master_y= y,
                                     w = 50, h = 50, color_background= (255,0,0),
                                     color_border= (255,0,255),
                                     onclick= self.btn_home_click,
                                     onclick_param= "",
                                     text="",
                                     font= "Verdana",
                                     font_size= 15,
                                     font_color= (0,255,0),
                                     path_image= "form/home.png")
        self.btn_1 = Button_Image(screen= self._slave,
                                     x= 100,
                                     y = 100,
                                     master_x= x,
                                     master_y= y,
                                     w = 50, h = 50, color_background= (255,0,0),
                                     color_border= (255,0,255),
                                     onclick= self.btn_home_click,
                                     onclick_param= 0,
                                     text="",
                                     font= "Verdana",
                                     font_size= 15,
                                     font_color= (0,255,0),
                                     path_image= "form/1.jpg")
        self.btn_2 = Button_Image(screen= self._slave,
                                     x= 200,
                                     y = 100,
                                     master_x= x,
                                     master_y= y,
                                     w = 50, h = 50, color_background= (255,0,0),
                                     color_border= (255,0,255),
                                     onclick= self.btn_home_click,
                                     onclick_param= 1,
                                     text="",
                                     font= "Verdana",
                                     font_size= 15,
                                     font_color= (0,255,0),
                                     path_image= "form/2.jpg")
        self.btn_3 = Button_Image(screen= self._slave,
                                     x= 280,
                                     y = 100,
                                     master_x= x,
                                     master_y= y,
                                     w = 50, h = 50, color_background= (255,0,0),
                                     color_border= (255,0,255),
                                     onclick= self.btn_home_click,
                                     onclick_param= 2,
                                     text="",
                                     font= "Verdana",
                                     font_size= 15,
                                     font_color= (0,255,0),
                                     path_image= "form/3.jpg")
        self.btn_4 = Button_Image(screen= self._slave,
                                     x= 380,
                                     y = 100,
                                     master_x= x,
                                     master_y= y,
                                     w = 50, h = 50, color_background= (255,0,0),
                                     color_border= (255,0,255),
                                     onclick= self.btn_home_click,
                                     onclick_param= 3,
                                     text="",
                                     font= "Verdana",
                                     font_size= 15,
                                     font_color= (0,255,0),
                                     path_image= "form/4.jpg")
        self.lista_widgets.append(self.btn_1)
        self.lista_widgets.append(self.btn_2)
        self.lista_widgets.append(self.btn_3)
        self.lista_widgets.append(self.btn_4)
        
    def btn_home_click(self,param):
        indice= int(param)
        self.nivel.establecer_nivel(indice)
        self.nivel.index = indice
        self.end_dialog()
        
    def update(self, lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos)
            self.draw()