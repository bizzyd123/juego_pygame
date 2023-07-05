import pygame
from pygame.locals import *
from form.GUI_button import *
from form.GUI_slider import *
from form.GUI_textbox import *
from form.GUI_label import *
from form.GUI_form import *
from form.GUI_button_image import *
from form.GUI_form_menu_score import *
from form.GUI_niveles import * 
from SqlLite.DataAccess import *
# esto es gui
class GUI_Menu (Form):
    
    def __init__(self,screen, x, y, w, h,juego, musica:str, color_background, color_border = "Black", border_size = -1, active = False):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        self.juego = juego
        self.volumen = 0.2
        self.volumen_efectos = 0.2
        self.flag_play = True
        pygame.mixer.init()
        self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray", "White", "Red", "Blue", 2, font = "Comic Sans", font_size= 15, font_color= "Black" )
        self.btn_play = Button(self._slave, x, y, 100, 100, 100, 50, "Green", "Blue", self.btn_play_click,"Nombre","Pause", font= "Verdana", font_size= 15, font_color= "White" )
        self.label_volumen = Label(self._slave, 650, 190, 100, 50, "20%", "Comic Sans", 15, "White", "form/Table.png")
        self.slider_volumen = Slider(self._slave, x, y, 100, 200, 300, 15,self.volumen, "Blue", "White")
        self.btn_tabla  = Button_Image(self._slave, x, y, 255, 100, 50, 50, "form/Menu_BTN.png", self.btn_tabla_click,"lalala")
        self.btn_nivel  = Button_Image(self._slave, x, y, 310, 100, 50, 50, "form/play2.png", self.btn_empezar_nivel,"lalala")
        self.slider_volumen_efectos = Slider(self._slave, x, y, 100, 300, 300, 15,self.volumen, "Blue", "White")
        self.label_volumen_efectos = Label(self._slave, 650, 290, 100, 50, "20%", "Comic Sans", 15, "White", "form/Table.png")
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_nivel)
        self.lista_widgets.append(self.slider_volumen_efectos)
        self.lista_widgets.append(self.label_volumen_efectos)
            
        pygame.mixer.music.load(f"Recursos/Sonidos/Musica/{musica}.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
    
        self.data_access = DataAccess("puntajes.db")

    def guardar_puntaje(self, puntaje):
        nombre = self.txtbox.get_text()
        if nombre is not None and nombre != '':
            self.data_access.insertar_puntaje(nombre,puntaje)
        else:
            raise ValueError("El jugador no cargo un nombre.")

    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen(lista_eventos)
                self.update_volumen_efectos(lista_eventos)
        else:
            self.hijo.update(lista_eventos)
    
    def render(self):
        self._slave.fill(self._color_background)
    
    def btn_empezar_nivel(self, texto):
        form_nivel = FromMenuNiveles(self._master,
                                     250,
                                     25,
                                     580,
                                     600,
                                     self.juego,
                                     (220,0,220),
                                     "White",
                                     True,
                                     "form/Window.png",
                                     None,
                                     100,
                                     10,
                                     10,
                                     
                                     )
        self.show_dialog(form_nivel)
    
    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color= "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color= "White"
            self.btn_play.set_text("Pause")
        self.flag_play = not self.flag_play
        
    def update_volumen(self, lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
    
    def update_volumen_efectos(self, lista_eventos):
        self.volumen_efectos = self.slider_volumen_efectos.value
        self.label_volumen_efectos.set_text(f"{round(self.volumen_efectos * 100)}%")
    
    def btn_tabla_click(self, texto):
        dic_score = self.data_access.obtener_puntajes()
        
        form_puntaje = FromMenuScore(self._master,
                                     250,
                                     25,
                                     500,
                                     550,
                                     (220,0,220),
                                     "White",
                                     True,
                                     "form/Window.png",
                                     dic_score,
                                     100,
                                     10,
                                     10
                                     )
        
        self.show_dialog(form_puntaje)
        