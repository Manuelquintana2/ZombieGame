import pygame
from pygame.locals import *

from api_forms.GUI_form import *
from api_forms.GUI_button_image import *
from api_forms.GUI_label import *
from api_forms.GUI_slider import *
from api_forms.GUI_picture_box import *


current_volume = 0.2

class FormPausa(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, contenedor_nivel=None):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.contenedor_nivel = contenedor_nivel
        self.volumen = current_volume  # Utiliza el volumen actual almacenado
        self.flag_play = True
       
        self.Pausa = PictureBox(self._slave, 200,50,450,140,"Pausa.jpg")
        self.fondo = PictureBox(self._slave, 0,0,900,700,"36278-split-split (1).png")
        self.btn_play = Button(self._slave, x, y, 150, 330, 100, 50, "Red", "Blue", self.btn_play_click, "Nombre", "Pausa", font="Verdana", font_size=15, font_color="White")
        self.label_volumen = Label(self._slave, 480, 380, 100, 50, f"{round(self.volumen * 100)}%", "Comic Sans", 15, "White", "api_forms\Table.png")
        self.slider_volumen = Slider(self._slave,x,y,150,400,300,10,self.volumen,"Blue","White")
        self.btn_home = Button_Image(screen=self._slave,
                                      master_x=self._x,
                                      master_y=self._y,
                                      x= 800,
                                      y=10,
                                      w=100,
                                      h=130,
                                      path_image="Reanudar.jpg",
                                      onclick=self.btn_home_click,
                                      onclick_param="",
                                      text="",
                                      font="Arial",
                                      )
      
        self.lista_widgets.append(self.fondo)      
        self.lista_widgets.append(self.btn_home)           
        self.lista_widgets.append(self.btn_play)
        self.lista_widgets.append(self.label_volumen)
        self.lista_widgets.append(self.slider_volumen)
        self.lista_widgets.append(self.Pausa)
        
    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cyan"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")
                
        self.flag_play = not self.flag_play
                    
    def update_volumen(self,lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volumen.set_text(f"{round(self.volumen * 100)}%")
        pygame.mixer.music.set_volume(self.volumen)
        
        # Actualiza la variable de volumen actual
        global current_volume
        current_volume = self.volumen
            
    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                    self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.fill(self._color_background)
    
    def btn_home_click(self,param):
        if self.contenedor_nivel != None:
            self.contenedor_nivel.setting = False  # Establecer self.setting en False
            self.end_dialog()
        self.end_dialog()
        
       