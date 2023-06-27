import pygame
from pygame.locals import *
from niveles.modo import *
from niveles.clases import *
from niveles.nivel import Nivel

class NivelTres(Nivel):
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
        fondo = pygame.image.load("Fondos\PNG\War2\Bright\War2.png")
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
        mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 10)

        #ITEMS
        item = Item((30,30), "Objetos-Iconos/PNG/Bonus_Items/HP_Bonus_03.png")
        lista_items = [item.lados]
        listaItems = [item]

        #MONEDAS
        moneda = Item((30,30),"Objetos-Iconos\PNG\Bonus_Items\Coin_03.png")
        moneda_dos = Item((30,30),"Objetos-Iconos\PNG\Bonus_Items\Coin_03.png")
        moneda_tres = Item((30,30),"Objetos-Iconos\PNG\Bonus_Items\Coin_03.png")
        lista_monedas = []
        lista_lados_monedas = []
        
        lista_monedas.append(moneda)
        lista_monedas.append(moneda_dos)
        lista_monedas.append(moneda_tres)
        
        lista_lados_monedas.append(moneda.lados)
        lista_lados_monedas.append(moneda_dos.lados)
        lista_lados_monedas.append(moneda_tres.lados)
        ##################################
        #OBJETIVO
        tamaño_objetivo = (60,60)
        posicion_inicial_objetivo = (30,70)
        objetivo = Objetivo(tamaño_objetivo,posicion_inicial_objetivo,"cerebro-humano-mano-zombie\cerebro.png")
        lista_objetivos = [objetivo.lados]
        listaObjetivo = [objetivo]
        #Enemigo
        posicion_inicial_enemigo = (50,250)
        tamaño_enemigo = (160,115)

        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["camina_derecha"] = enemigo_derecha
        diccionario_animaciones_enemigo["camina_izquierda"] = enemigo_izquierda
        diccionario_animaciones_enemigo["salta"] = enemigo_cae

        diccionario_animaciones_enemigo_dos = {}
        diccionario_animaciones_enemigo_dos["camina_derecha"] = enemigo_dos_derecha
        diccionario_animaciones_enemigo_dos["camina_izquierda"] = enemigo_dos_izquierda
        diccionario_animaciones_enemigo_dos["salta"] = enemigo_cae
        
        diccionario_animaciones_enemigo_tres = {}
        diccionario_animaciones_enemigo_tres["camina_derecha"] = enemigo_tres_derecha
        diccionario_animaciones_enemigo_tres["camina_izquierda"] = enemigo_tres_izquierda
        diccionario_animaciones_enemigo_tres["salta"] = enemigo_cae
        
        
        enemigo = Enemigo((420,0),(100,260),tamaño_enemigo,diccionario_animaciones_enemigo_dos,posicion_inicial_enemigo,10)
        enemigo_dos = Enemigo((800, 20),(450,560),tamaño_enemigo,diccionario_animaciones_enemigo,(400,550),10)
        enemigo_tres = Enemigo((420,0),(250,40),tamaño_enemigo,diccionario_animaciones_enemigo_tres,(200,30),10)
        lista_hitbox_enemigo = [enemigo.lados_hitbox, enemigo_dos.lados_hitbox,enemigo_tres.lados_hitbox]
        lista_enemigos = [enemigo.lados, enemigo_dos.lados,enemigo_tres.lados]
        listaEnemigo = [enemigo, enemigo_dos,enemigo_tres]
        

        #PLATAFORMAS
        piso = pygame.Rect(0,0,W,20)
        piso.top = mi_personaje.lados["main"].bottom
        lados_piso = obtener_rectangulo(piso)

        tamaño_plataformas = (100,50)

        plataforma = Plataforma(tamaño_plataformas, "Objetos-Iconos\PNG\Pads\Pad_02_1.png",(550,450))
        otra_plataforma = Plataforma((500,40), "Objetos-Iconos\PNG\Pads\Pad_02_1.png",(20,350))
        plataforma_objetivo = Plataforma((500,60), "Objetos-Iconos\PNG\Pads\Pad_02_1.png",(10,120))
        plataforma_4 = PlataformaAndante(5,"x",(400,750),(130,40), "Objetos-Iconos\PNG\Pads\Pad_02_1.png",(680,290))
        plataforma_movimiento = PlataformaAndante(8,"x",(650,750),(120,45), "Objetos-Iconos\PNG\Pads\Pad_02_1.png",(650,550))
        plataforma_5 = Plataforma((120,40),"Objetos-Iconos\PNG\Pads\Pad_02_1.png",(780,180))
        #PLATAFORMA TRAMPAS
        trampa = PlataformaTrampa((130,40),"Objetos-Iconos\PNG\Pads\Pad_02_2.png",(540,170),2)
        trampa_2 = PlataformaTrampa((120,80),"Objetos-Iconos\PNG\Pads\Pad_02_2.png",(780,470),2)
 
        lista_trampas = [trampa,trampa_2]
        listaTrampa = [trampa.lados,trampa_2.lados]
        lista_plataformas = [plataforma_5.lados,lados_piso,plataforma.lados,otra_plataforma.lados,plataforma_4.lados,
                            plataforma_objetivo.lados, plataforma_movimiento.lados,trampa.lados]

        listaPlataforma = [plataforma_5,plataforma,otra_plataforma,plataforma_objetivo,plataforma_4,plataforma_movimiento]
        
        
        super().__init__(pantalla, mi_personaje,
                         listaPlataforma,listaEnemigo,
                         lista_hitbox_enemigo,listaItems,
                         listaObjetivo,fondo_final,
                         lista_plataformas,lista_items,
                         lista_enemigos,lista_objetivos,
                         lista_trampas,listaTrampa,lista_balas,
                         lista_lados_balas,
                         lista_monedas,lista_lados_monedas)
