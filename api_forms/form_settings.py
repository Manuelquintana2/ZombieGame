import pygame
from pygame.locals import *

from api_forms.GUI_form import *
from api_forms.GUI_button_image import *
from api_forms.GUI_label import *
from api_forms.GUI_slider import *

class formSettings(Form):
        def __init__(self, screen, x, y, w, h, color_background, color_border, active):
            super().__init__(screen, x, y, w, h, color_background, color_border, active)
            self.volumen = 0.2
            self.flag_play = True
            self.btn_play = Button(self._slave, x, y, 100, 300, 100, 50, "Red", "Blue", self.btn_play_click, "Nombre", "Pausa", font="Verdana", font_size=15, font_color="White")
            self.label_volumen = Label(self._slave, 650, 390, 100, 50, "20%", "Comic Sans", 15, "White", "api_forms\Table.png")
            self.slider_volumen = Slider(self._slave,x,y,100,400,500,15,self.volumen,"Blue","White")
            self.btn_home = Button_Image(screen=self._slave,
                                          master_x= self._x,
                                          master_y= self._y,
                                          x = self._w-100,
                                          y =self._h-100,
                                          w = 100,
                                          h = 100,
                                          path_image="api_forms\home.png",
                                          onclick= self.btn_home_click,
                                          onclick_param="",
                                          text="Home",
                                          font="Arial",
                                          )
        
            self.lista_widgets.append(self.btn_home)
            
            self.lista_widgets.append(self.btn_play)
            self.lista_widgets.append(self.label_volumen)
            self.lista_widgets.append(self.slider_volumen)
            
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
            self.end_dialog()
        
        





            
            
            
            
            
            
            