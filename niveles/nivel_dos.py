import pygame
from pygame.locals import *
from niveles.modo import *
from niveles.clases import *
from niveles.nivel import Nivel

class NivelDos(Nivel):
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
        fondo = pygame.image.load("Fondos\PNG\War1\Pale\War.png")
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
        posicion_inicial_objetivo = (550,200)
        objetivo = Objetivo(tamaño_objetivo,posicion_inicial_objetivo,"cerebro-humano-mano-zombie\cerebro.png")
        lista_objetivos = [objetivo.lados]
        listaObjetivo = [objetivo]
        #Enemigo
        posicion_inicial_enemigo = (400, 370)
        tamaño_enemigo = (160,115)

        diccionario_animaciones_enemigo_dos = {}
        diccionario_animaciones_enemigo_dos["camina_derecha"] = enemigo_dos_derecha
        diccionario_animaciones_enemigo_dos["camina_izquierda"] = enemigo_dos_izquierda
        diccionario_animaciones_enemigo_dos["salta"] = enemigo_cae
        
        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["camina_derecha"] = enemigo_derecha
        diccionario_animaciones_enemigo["camina_izquierda"] = enemigo_izquierda
        diccionario_animaciones_enemigo["salta"] = enemigo_cae

        enemigo = Enemigo((500, 140),(450,380),tamaño_enemigo,diccionario_animaciones_enemigo_dos,posicion_inicial_enemigo,10)
        enemigo_dos = Enemigo((800, 20),(450,560),tamaño_enemigo,diccionario_animaciones_enemigo,(400,550),18)
        lista_hitbox_enemigo = [enemigo.lados_hitbox, enemigo_dos.lados_hitbox]
        lista_enemigos = [enemigo.lados, enemigo_dos.lados]
        listaEnemigo = [enemigo, enemigo_dos]

        #PLATAFORMAS
        piso = pygame.Rect(0,0,W,20)
        piso.top = mi_personaje.lados["main"].bottom
        lados_piso = obtener_rectangulo(piso)

        tamaño_plataformas = (200,50)

        plataforma = Plataforma(tamaño_plataformas, "Objetos-Iconos\PNG\Pads\Pad_03_1.png",(700,550))
        otra_plataforma = Plataforma((400,100), "Objetos-Iconos\PNG\Pads\Pad_03_1.png",(200,450))
        plataforma_objetivo = Plataforma((tamaño_plataformas), "Objetos-Iconos\PNG\Pads\Pad_03_1.png",(450,250))
        plataforma_4 = Plataforma((130,50), "Objetos-Iconos\PNG\Pads\Pad_03_1.png",(250,300))
        plataforma_movimiento = PlataformaAndante(8,"x",(10,100),(120,45), "Objetos-Iconos\PNG\Pads\Pad_03_1.png",(20,400))
        #PLATAFORMA TRAMPAS
        trampa = PlataformaTrampa((200,80),"Objetos-Iconos\PNG\Pads\Pad_03_2.png",(699,250),2)
        lista_trampas = [trampa]
        listaTrampa = [trampa.lados]
        lista_plataformas = [lados_piso,plataforma.lados,otra_plataforma.lados,plataforma_4.lados,
                                    plataforma_objetivo.lados, plataforma_movimiento.lados,trampa.lados]

        listaPlataforma = [plataforma,otra_plataforma,plataforma_objetivo,plataforma_4,plataforma_movimiento]
        
        
        super().__init__(pantalla, mi_personaje,
                         listaPlataforma,listaEnemigo,
                         lista_hitbox_enemigo,listaItems,
                         listaObjetivo,fondo_final,
                         lista_plataformas,lista_items,
                         lista_enemigos,lista_objetivos,
                         lista_trampas,listaTrampa,lista_balas,
                         lista_lados_balas,
                         lista_monedas,lista_lados_monedas)
