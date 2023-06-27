import pygame
from clases import *
from config import *
from modo import *

###############################################################
def actualizar_pantalla(pantalla,un_personaje:Personaje,
    fondo,lista_plataformas,lista_items, 
    lista_hitbox, lista_enemigos,
    Objetivo):
    
    pantalla.blit(fondo, (0,0))
    #Items
    item.update(pantalla)
    un_personaje.update(pantalla, lista_plataformas, lista_items, 
    lista_hitbox,lista_enemigos,
    objetivo)
    #Plataformas
    plataforma_movimiento.update(pantalla)
    plataforma.update(pantalla)
    otra_plataforma.update(pantalla)
    plataforma_4.update(pantalla)
    plataforma_objetivo.update(pantalla)
    #Enemigos
    enemigo.update(pantalla)
    #Objetivo
    objetivo.update(pantalla)
    
###############################################################


ANCHO = 900
ALTO = 700
FPS = 15
ventana = (ANCHO,ALTO)
flag = True

pygame.init()
RELOJ = pygame.time.Clock()

PANTALLA = pygame.display.set_mode((ventana))
velocidad = 10

#ICONO
icono = pygame.image.load("palanquita_mando.png")
pygame.display.set_icon((icono))

#FONDO_MENU
fondo = pygame.image.load("Fondos/PNG/War4/0000.png")
fondo_final = pygame.transform.scale(fondo, ventana)
PANTALLA.blit(fondo_final,(0,0))


#MUSICA
# pygame.mixer.music.load("")
# pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.09)

#Personaje
posicion_inicial = (50, 570)
tamaño = (75, 85)
diccionario_animaciones = {}
diccionario_animaciones["quieto"] = personaje_quieto
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda

mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 10)

#ITEMS
item = Item((30,30), "Objetos-Iconos/PNG/Bonus_Items/HP_Bonus_03.png")
lista_items = [item.lados]

##################################
#OBJETIVO
tamaño_objetivo = (60,60)
posicion_inicial_objetivo = (670,165)
objetivo = Objetivo(tamaño_objetivo,posicion_inicial_objetivo,"cerebro-humano-mano-zombie\cerebro.png")

#Enemigo
posicion_inicial_enemigo = (500, 350)
tamaño_enemigo = (160,115)

diccionario_animaciones_enemigo = {}
diccionario_animaciones_enemigo["camina_derecha"] = enemigo_derecha
diccionario_animaciones_enemigo["camina_izquierda"] = enemigo_izquierda
diccionario_animaciones_enemigo["salta"] = enemigo_cae

enemigo = Enemigo((780, 450),tamaño_enemigo,diccionario_animaciones_enemigo,posicion_inicial_enemigo,10)
lista_hitbox_enemigo = [enemigo.lados_hitbox]
lista_enemigo = [enemigo.lados]

#PLATAFORMAS
piso = pygame.Rect(0,0,ANCHO,20)
piso.top = mi_personaje.lados["main"].bottom
lados_piso = obtener_rectangulo(piso)

tamaño_plataformas = (200,50)

plataforma = Plataforma(tamaño_plataformas, "Objetos-Iconos/PNG/Pads/Pad_01_1.png",(150,550))
otra_plataforma = Plataforma((400,100), "Objetos-Iconos/PNG/Pads/Pad_01_1.png",(500,450))
plataforma_objetivo = Plataforma((tamaño_plataformas), "Objetos-Iconos/PNG/Pads/Pad_01_1.png",(570,220))
plataforma_4 = Plataforma((130,50), "Objetos-Iconos/PNG/Pads/Pad_01_1.png",(760,350))
plataforma_movimiento = PlataformaAndante(8,"y",(100,592),tamaño_plataformas, "Objetos-Iconos/PNG/Pads/Pad_01_1.png",(600,600))
lista_plataformas_quietas = [lados_piso,plataforma_movimiento.lados,plataforma.lados,otra_plataforma.lados,plataforma_4.lados, plataforma_objetivo.lados]



#IMAGEN VIDAS
# vida_1 = pygame.image.load("Objetos-Iconos\PNG\Bonus_Items\HP_Bonus_01.png")
# vida_1 = pygame.transform.scale(vida_1,(50,50))
# rectangulo_vida = vida_1.get_rect()
# rectangulo_vida.x = 50
# rectangulo_vida.y = 50

while flag:
    RELOJ.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            cambiar_modo()
                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        mi_personaje.que_hace = "derecha"
    elif keys[pygame.K_LEFT]:
        mi_personaje.que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"
    else:
        mi_personaje.que_hace = "quieto"
        
    actualizar_pantalla(PANTALLA, 
    mi_personaje, fondo_final, 
    lista_plataformas_quietas, lista_items,
    lista_hitbox_enemigo,
    lista_enemigo,objetivo.lados)
    
    if get_mode():
        for lado in lados_piso:
            pygame.draw.rect(PANTALLA, "Orange", lados_piso[lado] , 2)
        
        for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA,"Red", mi_personaje.lados[lado], 2)
            
        for lado in plataforma.lados:
            pygame.draw.rect(PANTALLA,"Yellow", plataforma.lados[lado], 2)
        
        for lado in plataforma_movimiento.lados:
            pygame.draw.rect(PANTALLA,"Yellow", plataforma_movimiento.lados[lado], 2)

        for lado in enemigo.lados_hitbox:
            pygame.draw.rect(PANTALLA,"Red", enemigo.lados_hitbox[lado], 2)
        
        for lado in enemigo.lados:
            pygame.draw.rect(PANTALLA,"Red", enemigo.lados[lado], 2)
        
        for lado in otra_plataforma.lados:
            pygame.draw.rect(PANTALLA,"Yellow", otra_plataforma.lados[lado], 2)
        
        for lado in plataforma_4.lados:
            pygame.draw.rect(PANTALLA,"Yellow", plataforma_4.lados[lado], 2)
        
        for lado in plataforma_objetivo.lados:
            pygame.draw.rect(PANTALLA,"Yellow", plataforma_objetivo.lados[lado], 2)
        
        for lado in item.lados:
            pygame.draw.rect(PANTALLA,"Blue", item.lados[lado], 2)
            
        for lado in objetivo.lados:
            pygame.draw.rect(PANTALLA,"Blue", objetivo.lados[lado], 2)
            
            
    pygame.display.update()
    
    



        



