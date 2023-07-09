import pygame
from pygame.locals import *

from api_forms.GUI_form import *
from api_forms.GUI_button_image import *
from api_forms.GUI_menu_pausa import *

class FormContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), color_background='sakjs')
        nivel._slave = self._slave
        self.nivel = nivel
        self.setting = False
        self._btn_home = Button_Image(screen=self._slave,
                                        master_x = self._x,
                                        master_y = self._y,
                                        x = self._w - 100,
                                        y = self._h - 100,
                                        w = 50,
                                        h = 50,
                                        color_background= (250,0,0),
                                        color_border= (255,0,255),
                                        onclick= self.btn_home_click,
                                        onclick_param= "",
                                        text= "",
                                        font= "Verdana",
                                        font_size= 15,
                                        font_color= (0,255,0),
                                        path_image= 'api_forms\home.png' )
        
        self._btn_settings = Button_Image(screen=self._slave,
                                 master_x= self._x,
                                 master_y= self._y,
                                 x=800,
                                 y=10,
                                 w=90,
                                 h=100,
                                 path_image="36278-split-split-split-removebg-preview.png",
                                 onclick=self.btn_settings_click,
                                 onclick_param="settings")
        
        self.lista_widgets.append(self._btn_settings)
        self.lista_widgets.append(self._btn_home)

    
    def update(self, lista_evento):
        if self.setting == False:
            self.nivel.update(lista_evento)
            for widget in self.lista_widgets:
                widget.update(lista_evento)
            self.draw()
        else:
            if self.verificar_dialog_result():
                for widget in self.lista_widgets:
                    widget.update(lista_evento)
                self.draw()
            else:
                self.hijo.update(lista_evento)

    # def update_setting(self, lista_eventos):
    #     if self.verificar_dialog_result():
    #         for widget in self.lista_widgets:
    #             widget.update_setting(lista_eventos)
                
    #         self.draw()
    #     else:
    #         self.hijo.update_setting(lista_eventos)
        
    def btn_settings_click(self, text):
        formulario_setting = FormPausa(self._master, 0, 0, 900, 700, "Black", "Black", True, self)  
        self.setting = True 
        self.show_dialog(formulario_setting)

    def btn_home_click(self, param):
        self.end_dialog()
