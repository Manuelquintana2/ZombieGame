import pygame
from pygame.locals import *

from api_forms.GUI_form import *
from api_forms.GUI_button_image import *
from api_forms.GUI_label import *
from api_forms.GUI_slider import *

class FormPausa(Form):
        def __init__(self, screen, x, y, w, h, color_background, color_border, active):
            super().__init__(screen, x, y, w, h, color_background, color_border, active)
        
                
        def update(self,lista_eventos):
            if self.verificar_dialog_result():
                if self.active:
                    self.draw()
                    self.render()
            else:
                self.hijo.update(lista_eventos)
        
    
        def render(self):
            self._slave.fill(self._color_background)
        
       