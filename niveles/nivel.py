import pygame
from niveles.modo import *

class Nivel:
    def __init__(self,pantalla,personaje_principal,
                 lista_plataformas,lista_enemigos,
                 enemigo_uno_hitbox,lista_items,
                 lista_objetivos,imagen_fondo,
                 lista_plataforma_lados,lista_items_lados,
                 enemigo_uno_lados,lista_objetivos_lados,
                 lista_trampa, lista_lados_trampa,lista_balas,
                 lista_lados_balas,lista_monedas,
                 lista_lados_monedas,
                 enemigo_dos_hitbox =None,enemigo_dos_lados=None,
                 enemigo_final = None, lista_balas_enemigo=None,lista_lados_balas_enemigo=None):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.imagen_fondo = imagen_fondo
        self.enemigos = lista_enemigos
        self.hitbox_enemigo_uno = enemigo_uno_hitbox
        self.items = lista_items
        self.objetivos = lista_objetivos
        self.plataformas_lados = lista_plataforma_lados
        self.items_lados = lista_items_lados
        self.enemigo_uno_lados = enemigo_uno_lados
        self.lista_objetivos_lados = lista_objetivos_lados
        self.lista_trampas = lista_trampa
        self.lista_lados_trampas = lista_lados_trampa
        self.proyectiles = lista_balas
        self.proyectiles_lados = lista_lados_balas
        self.monedas = lista_monedas
        self.monedas_lados = lista_lados_monedas
        self.enemigo_dos_hitbox = enemigo_dos_hitbox
        self.enemigo_dos_lados = enemigo_dos_lados
        self.enemigo_final = enemigo_final
        self.proyectiles_enemigo = lista_balas_enemigo
        self.lados_proyectiles_enemigo = lista_lados_balas_enemigo
    
    def update(self,lista_eventos):
        for event in lista_eventos:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    cambiar_modo()
                
        self.leer_inputs()
        self.actualizar_pantalla()
        self.dibujar_rectangulos()
    
    def actualizar_pantalla(self):
        self._slave.blit(self.imagen_fondo, (0,0))
        fuente = pygame.font.SysFont("helvetica",50)
        #IMAGEN VIDAS
        vida_imagen = pygame.image.load("Objetos-Iconos\PNG\Bonus_Items\HP_Bonus_03.png")
        vida_imagen = pygame.transform.scale(vida_imagen,(50,50))
        vidas = fuente.render("{0}".format(self.jugador.contador_vidas), True, (241, 196, 15))
        #IMAGEN PUNTAJE
        puntaje_imagen = pygame.image.load("Objetos-Iconos\PNG\Bonus_Items\Coin_03.png")
        puntaje_imagen = pygame.transform.scale(puntaje_imagen,(50,50))
        puntaje = fuente.render("{0}".format(self.jugador.contador_puntaje), True, (241, 196, 15))
        #IMAGEN PROYECTIL
        proyectil_imagen = pygame.image.load("PNG\Objects_separately\Rock1_1_no_shadow.png")
        proyectil_imagen = pygame.transform.scale(proyectil_imagen,(50,50))        
        proyectiles = fuente.render("{0}".format(self.jugador.contador_proyectiles),True,(241, 196, 15))
        #IMAGEN BOSS
        if self.enemigo_final != None:
            boss_final = pygame.image.load("Enemigos\_SCML/3/3_head.png")
            boss_final = pygame.transform.scale(boss_final,(50,50))
            boss = fuente.render("{0}".format(self.enemigo_final.vidas),True,(241, 196, 15))
            self._slave.blit(boss_final,(500,10))
            self._slave.blit(boss,(550,8))
        self._slave.blit(vida_imagen,(10,10))
        self._slave.blit(puntaje_imagen,(110,10))
        self._slave.blit(proyectil_imagen,(250,10))
        self._slave.blit(puntaje,(170,8))
        self._slave.blit(vidas,(70,8))
        self._slave.blit(proyectiles,(320,8))
        #Items
        for item in self.items:
            item.update(self._slave)
        #MONEDAS
        for monedas in self.monedas:
            monedas.update(self._slave)
            
        self.jugador.update(self._slave, self.plataformas_lados,
                            self.items_lados,self.hitbox_enemigo_uno,
                            self.enemigo_uno_lados,self.lista_objetivos_lados,
                            self.lista_lados_trampas,self.lista_trampas,
                            self.proyectiles_lados,self.monedas_lados,
                            self.enemigo_dos_hitbox,self.enemigo_dos_lados,
                            self.lados_proyectiles_enemigo)
        
        #Objetivo
        for objetivos in self.objetivos:
            objetivos.update(self._slave)
            
        #TRAMPAS
        for trampas in self.lista_trampas:
            trampas.update(self._slave)
        #Plataformas
        for plataformas in self.plataformas:
            plataformas.update(self._slave)
        #PROYECTILES
        for proyectiles in self.proyectiles:
            proyectiles.update(self._slave)
            
        if self.proyectiles_enemigo != None:
            for proyectiles in self.proyectiles_enemigo:
                proyectiles.update(self._slave)
        #Enemigos
        for enemigo in self.enemigos:
            enemigo.update(self._slave)
            
        if self.enemigo_final  != None:
            self.enemigo_final.update(self._slave,self.jugador,self.proyectiles)
        
    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.jugador.que_hace = "derecha"
        elif keys[pygame.K_LEFT]:
            self.jugador.que_hace = "izquierda"
        elif keys[pygame.K_UP]:
            self.jugador.que_hace = "salta"
        elif keys[pygame.K_SPACE] and self.jugador.contador_proyectiles > 0:
            self.jugador.que_hace = "disparar"
            self.jugador.contador_proyectiles -= 1
        else:
            self.jugador.que_hace = "quieto"
        
    
    def dibujar_rectangulos(self):
        if get_mode():
            for plataforma in self.plataformas:
                for lado in plataforma.lados:
                    pygame.draw.rect(self._slave,"Yellow", plataforma.lados[lado], 2)              

            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave,"Yellow", self.jugador.lados[lado], 2)
            
            for enemigo in self.enemigos:
                for lado in enemigo.lados:
                    pygame.draw.rect(self._slave,"Red", enemigo.lados[lado], 2)
                    
           
            for enemigo in self.enemigos:
                for lado in enemigo.lados_hitbox:
                        pygame.draw.rect(self._slave,"Red", enemigo.lados_hitbox[lado], 2)
            
            for item in self.items:
                for lado in item.lados:
                    pygame.draw.rect(self._slave,"Blue", item.lados[lado], 2)
                
            for objetivo in self.objetivos:
                for lado in objetivo.lados:
                    pygame.draw.rect(self._slave,"Blue", objetivo.lados[lado], 2)
            if self.enemigo_final != None:
                for lado in self.enemigo_final.lados:
                    pygame.draw.rect(self._slave,"Blue", self.enemigo_final.lados[lado], 2)
            
            if self.enemigo_final != None:
                for lado in self.enemigo_final.lados_hitbox:
                    pygame.draw.rect(self._slave,"Blue", self.enemigo_final.lados_hitbox[lado], 2)
            if self.enemigo_final != None:
                pygame.draw.rect(self._slave,"Blue", self.enemigo_final.hitbox_disparos,2)
                
           
    