import pygame
from pygame.locals import *

from api_forms.GUI_form import *
from api_forms.GUI_label import *
from api_forms.GUI_button_image import *

class formMenuScore(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path,score, margen_y, margen_x, espacio):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        
        aux_imagen = pygame.image.load(path)
        aux_imagen = pygame.transform.scale(aux_imagen,(w, h))
        
        self._slave = aux_imagen
        self.score = score
        
        self.margen_y = margen_y
        
        label_jugador = Label(self._slave, x=margen_x + 10, y= 20, w=300, h= 90,
                       text="Jugador", font="Verdana", font_size=30,font_color="White",path_image="api_forms/bar.png")
        label_puntaje = Label(self._slave, x=300, y= 20, w=300, h= 90,
                       text="Puntaje", font="Verdana", font_size=30,font_color="White",path_image="api_forms/bar.png")
        
        label_vidas = Label(self._slave, x=600, y= 20, w=300, h= 90,
                       text="Vidas", font="Verdana", font_size=30,font_color="White",path_image="api_forms/bar.png")
        
        self.lista_widgets.append(label_jugador)
        self.lista_widgets.append(label_puntaje)
        self.lista_widgets.append(label_vidas)
        
        pos_inicial_y = margen_y
        
        for j in self.score:
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = ""
                cadena = f"{s}"
                jugador = Label(self._slave, pos_inicial_x, pos_inicial_y, w/3 - margen_x, 100, cadena,
                                "Verdana", 30, "White", "api_forms\Table.png")
                self.lista_widgets.append(jugador)
                pos_inicial_x += w/3 
            pos_inicial_y += 100 + espacio
            
        self._btn_home = Button_Image(screen=self._slave,
                                    x = w-70,
                                    y = h-70,
                                    master_x= x,
                                    master_y= y,
                                    w = 50,
                                    h = 50,
                                    color_background=(255,0,0),
                                    onclick= self.btn_home_click,
                                    onclick_param="",
                                    text= "",
                                    font = "Verdana",
                                    font_size= 15,
                                    font_color=(0,255,0),
                                    path_image="api_forms\home.png")
        
        self.lista_widgets.append(self._btn_home)
        
    def btn_home_click(self,param):
        self.end_dialog()
        
    
    def update(self, lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos)
            self.draw()
        
        
        
        
        
        
        
        