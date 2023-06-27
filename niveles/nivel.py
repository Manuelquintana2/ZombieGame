import pygame
from niveles.modo import *

class Nivel:
    def __init__(self,pantalla,personaje_principal,
                 lista_plataformas,lista_enemigos,
                 lista_hitbox_enemigos,lista_items,
                 lista_objetivos,imagen_fondo,
                 lista_plataforma_lados,lista_items_lados,
                 lista_enemigos_lados,lista_objetivos_lados,
                 lista_trampa, lista_lados_trampa,lista_balas,
                 lista_lados_balas,lista_monedas,
                 lista_lados_monedas):
        self._slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.imagen_fondo = imagen_fondo
        self.enemigos = lista_enemigos
        self.hitbox_enemigos = lista_hitbox_enemigos
        self.items = lista_items
        self.objetivos = lista_objetivos
        self.plataformas_lados = lista_plataforma_lados
        self.items_lados = lista_items_lados
        self.lista_enemigos_lados = lista_enemigos_lados
        self.lista_objetivos_lados = lista_objetivos_lados
        self.lista_trampas = lista_trampa
        self.lista_lados_trampas = lista_lados_trampa
        self.proyectiles = lista_balas
        self.proyectiles_lados = lista_lados_balas
        self.monedas = lista_monedas
        self.monedas_lados = lista_lados_monedas
    
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
        puntaje = fuente.render("Score: {0}".format(self.jugador.contador_puntaje), True, (255,0,0))
        vidas = fuente.render("Vidas: {0}".format(self.jugador.contador_vidas), True, (255,0,0))
        proyectiles = fuente.render("Proyectiles: {0}".format(self.jugador.contador_proyectiles),True,(255,0,0))
        self._slave.blit(puntaje,(0,0))
        self._slave.blit(vidas,(0,50))
        self._slave.blit(proyectiles,(200,0))
        #Items
        for item in self.items:
            item.update(self._slave)
        #MONEDAS
        for monedas in self.monedas:
            monedas.update(self._slave)
            
        self.jugador.update(self._slave, self.plataformas_lados,
                            self.items_lados,self.hitbox_enemigos,
                            self.lista_enemigos_lados,self.lista_objetivos_lados,
                            self.lista_lados_trampas,self.lista_trampas,
                            self.proyectiles_lados,self.monedas_lados)
        #Plataformas
        for plataformas in self.plataformas:
            plataformas.update(self._slave)
        #Enemigos
        for enemigo in self.enemigos:
            enemigo.update(self._slave)
        #Objetivo
        for objetivos in self.objetivos:
            objetivos.update(self._slave)
            
        #TRAMPAS
        for trampas in self.lista_trampas:
            trampas.update(self._slave)
        #PROYECTILES
        for proyectiles in self.proyectiles:
            proyectiles.update(self._slave)
        
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
           