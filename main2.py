import pygame
from niveles.clases import *
from niveles.modo import *
from niveles.nivel_uno import NivelUno
from niveles.nivel_dos import NivelDos
from niveles.nivel_tres import NivelTres
from api_forms.GUI_form_prueba import FormPrueba

#PANTALLA
ANCHO = 900
ALTO = 700
FPS = 15
ventana = (ANCHO,ALTO)
flag = True

pygame.init()
RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((ventana))

form_principal = FormPrueba(PANTALLA,0,0,900,700, "Gold",5,True)

while flag:
    RELOJ.tick(FPS)
    PANTALLA.fill("Black")
    eventos = pygame.event.get()
    for event in eventos:
        if event.type == pygame.QUIT:
            flag = False
    
    form_principal.update(eventos)    
    
    pygame.display.update()