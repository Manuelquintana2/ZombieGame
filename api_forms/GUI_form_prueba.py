import pygame
from pygame.locals import *
import sqlite3
from api_forms.GUI_button import Button
from api_forms.GUI_slider import Slider
from api_forms.GUI_textbox import TextBox
from api_forms.GUI_label import Label
from api_forms.GUI_form import Form
from api_forms.GUI_button_image import Button_Image
from api_forms.GUI_form_score import formMenuScore
from api_forms.form_menu_niveles import formNiveles
from api_forms.form_settings import formSettings
from api_forms.GUI_picture_box import PictureBox
import json
from api_forms.form_lore import Lore


class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "Black", border_size = -1, active = True):
        super().__init__(screen,x,y,w,h,color_background,color_border,border_size,active)
        
        self.volumen = 0.2
        self.flag_play = True
        
        pygame.mixer.init()
        
        ######CONTROLES #####
        self.txtbox = TextBox(self._slave,x , y, 300, 50, 300, 30, "Gray","White","Red","Blue",2,font="Comic Sans", font_size=15, font_color="Black")
        self.btn_tabla = Button_Image(self._slave,x,y,420,110,280,150,"score.png",self.btn_tabla_click, "lala")
        self.btn_niveles = Button_Image(self._slave,x,y,200,130,200,100,"Play-Now-Button-PNG-Photos.png",self.btn_imagen_click, "niveles")
        self.btn_settings = Button_Image(self._slave,x,y,730,20,170,170,"zyro-image-PhotoRoom.png-PhotoRoom.png",self.btn_settings_click, "settings")
        self.picture_box = PictureBox(self._slave,0,0,900,720,"zyro-image2.png")
        self.btn_lore = Button_Image(self._slave,x,y,200,270,200,150,"historia.png",self.btn_narrativa_click, "Lore")
        ######
        
        #Agrego los controles a la lista
        self.lista_widgets.append(self.picture_box)
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_tabla)
        self.lista_widgets.append(self.btn_niveles)
        self.lista_widgets.append(self.btn_settings)
        self.lista_widgets.append(self.btn_lore)
        
        
        
        pygame.mixer.music.load("api_forms\Vengeance (Loopable).wav")  
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)
        
        self.render()
        
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
        
    
    def btn_imagen_click(self,text):
        formulario_niveles = formNiveles(self._master,0,0,900,700,"Black","Black",True,"zyro-image.png")
        self.show_dialog(formulario_niveles)
        
    def btn_settings_click(self,text):
        formulario_setting = formSettings(self._master,0,0,900,700,"Yellow","Blue",True)
        self.show_dialog(formulario_setting)
        
    def btn_narrativa_click(self,text):
        lore = Lore(self._master,0,0,900,700,"Yellow","Blue",True)
        self.show_dialog(lore)
    
    def btn_tabla_click(self,texto):
        puntaje_final = 0
        puntaje_nivel_uno = 0
        puntaje_nivel_dos = 0
        puntaje_nivel_tres = 0
        vidas_nivel_uno = 0
        vidas_nivel_dos = 0
        vidas_nivel_tres = 0
        vidas_finales = 0
        
        try:
            with open("datospartidanivel_uno.json","r") as file:
                puntuacion = json.load(file)
            
            valores_puntos_vidas = list(puntuacion.values())
            puntaje_nivel_uno = valores_puntos_vidas[0]
            vidas_nivel_uno = valores_puntos_vidas[1]
        
            with open("datospartidanivel_dos.json","r") as file2:
                puntuacion_dos = json.load(file2)
                
            valores_puntos_vidas = list(puntuacion_dos.values())
            puntaje_nivel_dos = valores_puntos_vidas[0]
            vidas_nivel_dos = valores_puntos_vidas[1]
                
            with open("datospartidanivel_tres.json","r") as file3:
                puntuacion_tres = json.load(file3)
                
            valores_puntos_vidas = list(puntuacion_tres.values())
            puntaje_nivel_tres = valores_puntos_vidas[0]
            vidas_nivel_tres = valores_puntos_vidas[1]
            
        except FileNotFoundError:
            estadoNivel = "No pasaste todos los niveles"
            print(estadoNivel)
        
        puntaje_final = puntaje_nivel_uno + puntaje_nivel_dos + puntaje_nivel_tres
        vidas_finales = vidas_nivel_uno + vidas_nivel_dos + vidas_nivel_tres
        nombre = self.txtbox.get_text()
            
        dic_score = [{"jugador": nombre, "Score": puntaje_final, "vidas": vidas_finales}
                    ]
        
        form_puntaje = formMenuScore(self._master,
                                    0,
                                    0,
                                    900,
                                    700,
                                    (220,0,220),
                                    "White",
                                    True,
                                    "api_forms\Window.png",
                                    dic_score,
                                    100,
                                    10,
                                    10)
        
        self.show_dialog(form_puntaje)
        # Crear una conexión a la base de datos
        conn = sqlite3.connect('datos_partida.db')

        # Crear un cursor para ejecutar consultas SQL
        cursor = conn.cursor()

        # Crear la tabla
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS datos_partida (
                jugador TEXT,
                puntuacion INTEGER,
                vidas INTEGER
            )
        ''')

        # Eliminar los datos anteriores de la tabla
        cursor.execute('''
            DELETE FROM datos_partida
        ''')

        # Insertar los nuevos datos en la tabla
        for score in dic_score:
            cursor.execute('''
                INSERT INTO datos_partida (jugador,puntuacion,vidas)
                VALUES (?, ?, ?)
            ''', (score["jugador"], score["Score"], score["vidas"]))

        # Guardar los cambios y cerrar la conexión
        conn.commit()
        conn.close()

        
        
    
        
        
        