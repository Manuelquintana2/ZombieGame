import pygame
from pygame.locals import *

from api_forms.GUI_form import *
from api_forms.GUI_button_image import *
from api_forms.GUI_label import *
from niveles.manejador_niveles import ManejadorNiveles
from api_forms.form_contenedor_niveles import FormContenedorNivel

class formNiveles(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.manejador_niveles = ManejadorNiveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        
        self.btn_nivel_uno = Button_Image(screen=self._slave,
                                          master_x= x,
                                          master_y= y,
                                          x = 200,
                                          y =120,
                                          w = 100,
                                          h = 100,
                                          path_image="api_forms\imagen_nivel_uno.png",
                                          onclick= self.entrar_nivel,
                                          onclick_param="nivel_uno",
                                          text="",
                                          font="Arial")
        
        self.btn_nivel_dos = Button_Image(screen=self._slave,
                                          master_x= x,
                                          master_y= y,
                                          x = 300,
                                          y =120,
                                          w = 100,
                                          h = 100,
                                          path_image="api_forms\imagen_nivel_dos.png",
                                          onclick= self.entrar_nivel,
                                          onclick_param="nivel_dos",
                                          text="",
                                          font="Arial")

        self.btn_nivel_tres = Button_Image(screen=self._slave,
                                          master_x= x,
                                          master_y= y,
                                          x = 400,
                                          y =120,
                                          w = 100,
                                          h = 100,
                                          color_background=(255,0,0),
                                          color_border=(255,0,255),
                                          path_image="api_forms\imagen_nivel_tres.png",
                                          onclick= self.entrar_nivel,
                                          onclick_param="nivel_tres",
                                          text="",
                                          font="Arial",
                                          font_size= 15,
                                          font_color=(0,255,0))

        self.btn_home = Button_Image(screen=self._slave,
                                          master_x= x,
                                          master_y= y,
                                          x = 200,
                                          y =300,
                                          w = 100,
                                          h = 100,
                                          path_image="api_forms\home.png",
                                          onclick= self.btn_home_click,
                                          onclick_param="",
                                          text="Home",
                                          font="Arial",
                                          )
        
        self.lista_widgets.append(self.btn_nivel_uno)
        self.lista_widgets.append(self.btn_nivel_dos)
        self.lista_widgets.append(self.btn_nivel_tres)
        self.lista_widgets.append(self.btn_home) 
        
    def on(self,parametro):
        print("hola",parametro)
        
    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
        else:
            self.hijo.update(lista_eventos)
    
    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        form_contenedor_nivel = FormContenedorNivel(self._master,nivel)
        self.show_dialog(form_contenedor_nivel)
    
    def btn_home_click(self,param):
        self.end_dialog()

        
        

    
    
    
    
    
    
    
          