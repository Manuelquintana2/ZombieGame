import pygame
from pygame.locals import *

from api_forms.GUI_form import *
from api_forms.GUI_button_image import *
from api_forms.GUI_picture_box import *

class Lore(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
    
    
        self.picture_box = PictureBox(self._slave,0,0,900,720,"Lore.png")
        self.btn_home = Button_Image(screen=self._slave,
                                            master_x= x,
                                            master_y= y,
                                            x = 800,
                                            y =10,
                                            w = 100,
                                            h = 100,
                                            path_image="api_forms\home.png",
                                            onclick= self.btn_home_click,
                                            onclick_param="",
                                            text="Home",
                                            font="Arial",
                                            )
        
        self.lista_widgets.append(self.picture_box)
        self.lista_widgets.append(self.btn_home)
    
    
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
    
    
    def render(self):
        self._slave.fill(self._color_background)
        

    def btn_home_click(self,param):
        self.end_dialog()

