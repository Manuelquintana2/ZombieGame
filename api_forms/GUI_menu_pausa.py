import pygame
from pygame.locals import *

from api_forms.GUI_form import *
from api_forms.GUI_button_image import *
from api_forms.GUI_label import *
from api_forms.GUI_slider import *
from api_forms.GUI_picture_box import *
from api_forms.form_settings import *

class FormPausa(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, contenedor_nivel=None):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.contenedor_nivel = contenedor_nivel
        
       
        self.Pausa = PictureBox(self._slave, 200,50,450,140,"Pausa.jpg")
        self.fondo = PictureBox(self._slave, 0,0,900,700,"36278-split-split (1).png")
        self.boton_settings = Button_Image(self._slave,self._x,self._y,
                                           200,300,160,180,
                                           "Musica-PhotoRoom.png-PhotoRoom.png",
                                           self.btn_settings_click,"","","Arial")
            
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
        self.lista_widgets.append(self.Pausa)
        self.lista_widgets.append(self.boton_settings)                    
    
            
    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)        
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.fill(self._color_background)
    
    def btn_home_click(self,param):
        if self.contenedor_nivel != None:
            self.contenedor_nivel.setting = False 
            self.end_dialog()
        self.end_dialog()
        
    def btn_settings_click(self,param):
        formulario_setting = formSettings(self._master,0,0,900,700,"Yellow","Blue",True)
        self.show_dialog(formulario_setting)
        
   
        
        
        
       