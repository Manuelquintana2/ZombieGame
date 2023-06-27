import pygame
from pygame.locals import *

from api_forms.GUI_form import *
from api_forms.GUI_button_image import *

class FormContenedorNivel(Form):
    def __init__(self,pantalla:pygame.Surface,nivel):
        super().__init__(pantalla,0,0,pantalla.get_width(),pantalla.get_height(),"White")
        nivel._slave = self._slave
        self.nivel = nivel
        
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
        
        
    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()
        
    def btn_home_click(self,param):
        self.end_dialog()
