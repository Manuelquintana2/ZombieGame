import pygame
from pygame.locals import *
from niveles.modo import *
from niveles.clases import *
from niveles.nivel import Nivel


class NivelUno(Nivel):
    def __init__(self, pantalla: pygame.Surface): 
        #PANTALLA
        W = pantalla.get_width()
        H = pantalla.get_height()
        
        flag = True

        velocidad = 10

        #ICONO
        icono = pygame.image.load("palanquita_mando.png")
        pygame.display.set_icon((icono))

        #FONDO_MENU
        fondo = pygame.image.load("Fondos/PNG/War4/0000.png")
        fondo_final = pygame.transform.scale(fondo, (W,H))
        pantalla.blit(fondo_final,(0,0))


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
        diccionario_animaciones["atacar"] = personaje_disparar
        mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 10,"nivel_uno")

        #ITEMS
        item = Item((30,30), "Objetos-Iconos/PNG/Bonus_Items/HP_Bonus_03.png")
        lista_items = [item.lados]
        listaItems = [item]
        
        #MONEDAS
        moneda = Item((30,30),"Objetos-Iconos\PNG\Bonus_Items\Coin_03.png")
        lista_monedas = []
        lista_lados_monedas = []
        
        lista_monedas.append(moneda)
        
        
        lista_lados_monedas.append(moneda.lados)
        
        

        ##################################
        #OBJETIVO
        tamaño_objetivo = (60,60)
        posicion_inicial_objetivo = (70,165)
        objetivo = Objetivo(tamaño_objetivo,posicion_inicial_objetivo,"cerebro-humano-mano-zombie\cerebro.png")
        lista_objetivos = [objetivo.lados]
        listaObjetivo = [objetivo]
        #Enemigo
        posicion_inicial_enemigo = (500, 350)
        tamaño_enemigo = (160,115)

        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["camina_derecha"] = enemigo_derecha
        diccionario_animaciones_enemigo["camina_izquierda"] = enemigo_izquierda
        diccionario_animaciones_enemigo["salta"] = enemigo_cae

        enemigo = Enemigo((780, 450),(550,360),tamaño_enemigo,diccionario_animaciones_enemigo,posicion_inicial_enemigo,10)
       
        
        listaEnemigo = [enemigo]
        

        #PLATAFORMAS
        piso = pygame.Rect(0,0,W,20)
        piso.top = mi_personaje.lados["main"].bottom
        lados_piso = obtener_rectangulo(piso)

        tamaño_plataformas = (200,50)

        plataforma = Plataforma(tamaño_plataformas, "Objetos-Iconos/PNG/Pads/Pad_01_1.png",(150,550))
        otra_plataforma = Plataforma((400,100), "Objetos-Iconos/PNG/Pads/Pad_01_1.png",(500,450))
        plataforma_objetivo = Plataforma((tamaño_plataformas), "Objetos-Iconos/PNG/Pads/Pad_01_1.png",(70,220))
        plataforma_4 = Plataforma((130,50), "Objetos-Iconos/PNG/Pads/Pad_01_1.png",(760,350))
        plataforma_movimiento = PlataformaAndante(8,"y",(100,592),tamaño_plataformas, "Objetos-Iconos/PNG/Pads/Pad_01_1.png",(600,600))
        plataforma_5 = Plataforma(tamaño_plataformas, "Objetos-Iconos/PNG/Pads/Pad_01_1.png",(450,250))
        #PLATAFORMA TRAMPA
        trampa = PlataformaTrampa((150,70), "Objetos-Iconos\PNG\Pads\Pad_01_2.png", (260,280), 1)
        lista_trampas = [trampa]
        listaTrampas = [trampa.lados]
        lista_plataformas = [lados_piso,plataforma_5.lados,plataforma.lados,otra_plataforma.lados,plataforma_4.lados,
                            plataforma_objetivo.lados,trampa.lados]

        listaPlataforma = [plataforma,plataforma_5,otra_plataforma,plataforma_objetivo,plataforma_4]

        super().__init__(pantalla, mi_personaje,
                         listaPlataforma,listaEnemigo,
                         enemigo.lados_hitbox,listaItems,
                         listaObjetivo,fondo_final,
                         lista_plataformas,lista_items,
                         enemigo.lados,lista_objetivos,
                         lista_trampas,listaTrampas,lista_balas,
                         lista_lados_balas,
                         lista_monedas,lista_lados_monedas)


    
