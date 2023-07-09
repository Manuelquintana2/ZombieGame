import pygame
from niveles.config import *
import random
import json

class Personaje:
    def __init__(self, pantalla,tamaño, animaciones, posicion_inicial,velocidad,nivel=None):
        #CONFECCION
        self._slave = pantalla
        self.nivel = nivel
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.gano = False
        #GRAVEDAD
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        #Animaciones
        self.contador_de_pasos = 0
        self.que_hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        self.rectangulo = pygame.Rect(self.animaciones["camina_derecha"][0].get_rect())
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        #MOVIMIENTO
        self.velocidad = velocidad
        self.desplazamiento_y = 0 
        self.esta_chocando_derecha = False
        self.esta_chocando_izquierda = False
        self.mira_derecha = True
        self.mira_izquierda = False
        #CONTADORES
        self.contador_vidas = 1
        self.contador_monedas = 0
        self.contador_puntaje = 0
        self.contador_proyectiles = 1
        
    #Quieto - Salta - Camina derecha - Camina izquierda
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave],(self.ancho, self.alto))
    
    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_de_pasos >= largo:
            self.contador_de_pasos = 0
            
        pantalla.blit(animacion[self.contador_de_pasos], self.lados["main"])
        self.contador_de_pasos += 1

    def mover(self, velocidad): 
        for lado in self.lados:
            self.lados[lado].x += velocidad
    
    def disparos(self):
        bala = Proyectil((10,10),"PNG\Objects_separately\Rock1_1_no_shadow.png",self.rectangulo.x,self.rectangulo.y,20)
        lista_balas.append(bala)
        lista_lados_balas.append(bala.lados)
        
    def aplicar_gravedad(self, pantalla,lista_plataformas):
        if self.esta_saltando == True:
            self.animar(pantalla, "salta")
            
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            
            if self.desplazamiento_y * self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
                
        for plataformas in lista_plataformas:
            if self.lados["bottom"].colliderect(plataformas["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = plataformas["main"].top 
                break
            elif self.lados["top"].colliderect(plataformas["bottom"]):
                self.desplazamiento_y = 2
                break
            else:
                self.esta_saltando = True
    
    def verificar_colisiones_plataformas(self, lista_plataformas):
        for plataformas in lista_plataformas:
            if self.lados["right"].colliderect(plataformas["left"]):
                self.esta_chocando_derecha = True
                break
            elif self.lados["left"].colliderect(plataformas["right"]):
                self.esta_chocando_izquierda = True
                break
            else:
                self.esta_chocando_derecha = False
                self.esta_chocando_izquierda = False

    def verificar_colision_moneda(self, lista_monedas):
        for item in lista_monedas:
            if self.lados["main"].colliderect(item["main"]):
                efectos_de_sonido("PC Computer - Star Wars Yoda Stories - Sound Effects\SWITCH-6.WAV")
                self.desaparecer_item(lista_monedas)
                self.contador_puntaje += 200
                
    def verificar_colision_item(self, lista_item):
        for item in lista_item:
            if self.lados["main"].colliderect(item["main"]):
                efectos_de_sonido("PC Computer - Star Wars Yoda Stories - Sound Effects\ARMFORCE.WAV")
                self.desaparecer_item(lista_item)
                self.contador_vidas += 1
                self.contador_puntaje += 100
                print(f"Ahora tienes {self.contador_vidas} vidas. Aprovechalas!")
    
    def verificar_colision_enemigo(self,lista_hitbox,lista_enemigo):
        if self.lados["right"].colliderect(lista_hitbox["left"]) and self.mira_derecha == True:
            self.contador_vidas -= 1
            efectos_de_sonido("PC Computer - Star Wars Yoda Stories - Sound Effects\HURT.WAV")
            print(f"Haz perdido una vida.")
        elif self.lados["left"].colliderect(lista_hitbox["right"]) and self.mira_izquierda == True and self.mira_derecha==False:
            self.contador_vidas -= 1
            efectos_de_sonido("PC Computer - Star Wars Yoda Stories - Sound Effects\HURT.WAV")
            print(f"Haz perdido una vida.")
        elif self.contador_vidas <= 0:
            self.desaparecer_personaje(self.lados)
               
        elif self.lados["bottom"].colliderect(lista_hitbox["top"]):
            efectos_de_sonido("PC Computer - Dragon Ball FighterZ - Android 18\Android #18\Default/vaen009.ogg")
            self.desaparecer_enemigo_uno(lista_hitbox,lista_enemigo)
            self.contador_puntaje += 100
            self.contador_proyectiles += 3
    
    def verificar_colision_enemigo_dos(self,enemigo_dos_hitbox,enemigo_dos):
        if enemigo_dos_hitbox and enemigo_dos != None:
            if self.lados["right"].colliderect(enemigo_dos_hitbox["left"]) and self.mira_derecha == True:
                self.contador_vidas -= 1
                efectos_de_sonido("PC Computer - Star Wars Yoda Stories - Sound Effects\HURT.WAV")
                print(f"Haz perdido una vida.")
            elif self.lados["left"].colliderect(enemigo_dos_hitbox["right"]) and self.mira_izquierda == True and self.mira_derecha==False:
                self.contador_vidas -= 1
                print(f"Haz perdido una vida.")
            elif self.contador_vidas <= 0:
                self.desaparecer_personaje(self.lados)
                
            elif self.lados["bottom"].colliderect(enemigo_dos_hitbox["top"]):
                efectos_de_sonido("PC Computer - Dragon Ball FighterZ - Android 18\Android #18\Default/vaen019.ogg")
                self.desaparecer_enemigo_dos(enemigo_dos_hitbox,enemigo_dos)
                self.contador_puntaje += 100
                self.contador_proyectiles += 3
        else:
            return None
    
    def verificar_colision_trampa(self,lista_trampas_lados,lista_trampas):
        for trampa in lista_trampas_lados:
            for trampas in lista_trampas:
                if self.lados["bottom"].colliderect(trampa["top"]):
                    self.contador_vidas -= trampas.daño
                elif self.contador_vidas <= 0:
                    self.desaparecer_personaje(self.lados)
                    break
    
    def desaparecer_item(self, lista_item:list):
        for item in lista_item:
            for lado in item:
                item[lado].x = -7000
                item[lado].y = 7000
    
    def desaparecer_personaje(self,rectangulo):
        for lado in rectangulo:
            rectangulo[lado].x = -10000
            rectangulo[lado].y = -10000
    
    def desaparecer_enemigo_uno(self, enemigo_uno_hitbox, enemigo_uno):
        for lado in enemigo_uno_hitbox:
            enemigo_uno_hitbox[lado].x = -5000
            enemigo_uno_hitbox[lado].y = -5000

        for lado in enemigo_uno:
            enemigo_uno[lado].x = -5000
            enemigo_uno[lado].y = -5000
            
    def desaparecer_enemigo_dos(self, enemigo_dos_hitbox, enemigo_dos):
        if enemigo_dos_hitbox != None:
            for lado in enemigo_dos_hitbox:
                enemigo_dos_hitbox[lado].x = -5000
                enemigo_dos_hitbox[lado].y = -5000

            for lado in enemigo_dos:
                enemigo_dos[lado].x = -5000
                enemigo_dos[lado].y = -5000
    


    def ganar_juego(self,lista_objetivo,enemigo_uno_hitbox,enemigo,enemigo_dos_hitbox,enemigo_dos,lista_item):
        for objetivo in lista_objetivo:
            if self.lados["main"].colliderect(objetivo["main"]):
                self.gano = True
                efectos_de_sonido("Recoome/vrkn003.ogg")
                self.contador_puntaje += 500
                self.desaparecer_enemigo_uno(enemigo_uno_hitbox, enemigo)
                self.desaparecer_enemigo_dos(enemigo_dos_hitbox, enemigo_dos)
                self.desaparecer_personaje(self.lados)
                self.desaparecer_item(lista_item)
                self.guardar_datos_partida()
                
                
    def guardar_datos_partida(self):
        nombre_archivo = f'datospartida{self.nivel}.json'
        datos = {
            
            'puntos': self.contador_puntaje,
            'vidas': self.contador_vidas
   
        }

        try:
            with open(nombre_archivo, 'w') as file:
                json.dump(datos, file, indent=4)
        except PermissionError:
            print('Completado todos los niveles, felicidades')            
                
    def verificar_colision_enemigo_bala(self, lista_hitbox,lista_enemigo,lista_bala):
        for bala in lista_bala:
            if bala["main"].colliderect(lista_hitbox["main"]):
                efectos_de_sonido("PC Computer - Dragon Ball FighterZ - Android 18\Android #18\Default/vaen009.ogg")
                self.desaparecer_enemigo_uno(lista_hitbox,lista_enemigo)
    
    def verificar_colision_enemigo_bala_dos(self, enemigo_dos_hitbox,enemigo_dos,lista_bala):
        if enemigo_dos_hitbox and enemigo_dos != None:
            for bala in lista_bala:
                if bala["main"].colliderect(enemigo_dos_hitbox["main"]):
                    efectos_de_sonido("PC Computer - Dragon Ball FighterZ - Android 18\Android #18\Default/vaen019.ogg")
                    self.desaparecer_enemigo_dos(enemigo_dos_hitbox,enemigo_dos)
        else:
            return None
        
    def verificar_colision_boss(self,lista_balas_enemigo):
        if lista_balas_enemigo != None:
            for bala in lista_balas_enemigo:
                if self.lados["main"].colliderect(bala["main"]):
                    efectos_de_sonido("PC Computer - Star Wars Yoda Stories - Sound Effects\HURT.WAV")
                    self.contador_vidas -= 1
        
    
    def update(self,pantalla,lista_plataformas, 
               lista_items,enemigo_uno_hitbox, 
               enemigo_uno,lista_objetivo,lista_trampas_lados,
               lista_trampas,lista_balas,lista_monedas,enemigo_dos_hitbox,
               enemigo_dos,balas_enemigo):
        match self.que_hace:     
            case "derecha":
                self.mira_derecha = True
                self.mira_izquierda = False
                if self.rectangulo.right < 900 - self.velocidad and not self.esta_chocando_derecha:
                    self.mover(self.velocidad)
                if self.esta_saltando == False:
                    self.animar(pantalla, "camina_derecha")
            case "izquierda":
                self.mira_derecha = True
                self.mira_derecha = False
                if self.rectangulo.left > 1 and not self.esta_chocando_izquierda:
                    self.mover(self.velocidad * -1)
                if self.esta_saltando == False:
                    self.animar(pantalla, "camina_izquierda")
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
            case "disparar":
                    self.animar(pantalla, "atacar")
                    self.disparos()
            case "quieto":
                self.mira_derecha = True
                self.mira_izquierda = True
                if self.esta_saltando == False:
                    self.animar(pantalla, "quieto")
                
        self.aplicar_gravedad(pantalla,lista_plataformas)
        self.verificar_colisiones_plataformas(lista_plataformas)
        self.verificar_colision_item(lista_items)
        self.verificar_colision_enemigo(enemigo_uno_hitbox,enemigo_uno)
        self.verificar_colision_enemigo_dos(enemigo_dos_hitbox,enemigo_dos)
        self.ganar_juego(lista_objetivo,enemigo_uno_hitbox,enemigo_uno,enemigo_dos_hitbox,enemigo_dos,lista_items)
        self.verificar_colision_trampa(lista_trampas_lados, lista_trampas)
        self.verificar_colision_enemigo_bala(enemigo_uno_hitbox,enemigo_uno,lista_lados_balas)
        self.verificar_colision_enemigo_bala_dos(enemigo_dos_hitbox,enemigo_dos,lista_balas)
        self.verificar_colision_moneda(lista_monedas)
        self.verificar_colision_boss(balas_enemigo)
        
class Proyectil(Personaje):
    def __init__(self,tamaño,path,posx,posy,velocidad):
        self.imagen_proyectil = pygame.image.load(path)
        self.imagen_proyectil = pygame.transform.scale(self.imagen_proyectil,(30,30))
        self.rect = self.imagen_proyectil.get_rect()
        self.velocidad_disparo = velocidad
        self.rect.x = posx
        self.rect.y = posy
        self.lados = obtener_rectangulo(self.rect)
            
    def update(self,pantalla):
        self.rect.x += self.velocidad_disparo
        pantalla.blit(self.imagen_proyectil,self.rect)

class Enemigo(Personaje):
    def __init__(self,de_donde_hasta_donde,posicion_hitbox,tamaño, animaciones, posicion_inicial,velocidad,pantalla):
        super().__init__(pantalla,tamaño, animaciones, posicion_inicial, velocidad)
        self.orientacion_enemigo = 1
        self.de_donde = de_donde_hasta_donde[0]
        self.hasta_donde = de_donde_hasta_donde[1]
        self.x_hitbox = posicion_hitbox[0]
        self.y_hitbox = posicion_hitbox[1]
        self.hitbox_real = pygame.Rect(self.x_hitbox,self.y_hitbox,70,100)
        self.lados_hitbox = obtener_rectangulo(self.hitbox_real)
        
        
    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_de_pasos >= largo:
            self.contador_de_pasos = 0
            
        pantalla.blit(animacion[self.contador_de_pasos], self.lados["main"])
        self.contador_de_pasos += 1
    
    def mover(self,rectangulo,hitbox_real):
        for lado in rectangulo:
            rectangulo[lado].x += self.velocidad * self.orientacion_enemigo
        if rectangulo[lado].x > self.de_donde or rectangulo[lado].x < self.hasta_donde:
            self.orientacion_enemigo = self.orientacion_enemigo * -1
            self.de_donde = self.de_donde
            self.hasta_donde = self.hasta_donde
        for lado in hitbox_real:
            hitbox_real[lado].x += self.velocidad * self.orientacion_enemigo
        if hitbox_real[lado].x > self.de_donde + 40 or hitbox_real[lado].x < self.hasta_donde +60:
            self.orientacion_enemigo = self.orientacion_enemigo * -1
            
    def update(self, pantalla):
        self.mover(self.lados,self.lados_hitbox)
        if self.orientacion_enemigo == 1:
            self.animar(pantalla, "camina_derecha")
        else:
            self.animar(pantalla, "camina_izquierda")
            
    
            
    
class Plataforma:
    def __init__(self, tamaño, path, posicion_inicial):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen,(self.ancho,self.alto))
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posicion_inicial[0]
        self.rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        
    
    def update(self,pantalla):
        pantalla.blit(self.imagen, self.rectangulo)

class PlataformaAndante(Plataforma):
    def __init__(self,velocidad,eje,de_donde_hasta_donde ,tamaño_andante, path_andante, posicion_inicial):
        super().__init__(tamaño_andante, path_andante, posicion_inicial)
        self.velocidad = velocidad
        self.orientacion_plataforma = 1
        self.eje = eje
        self.de_donde = de_donde_hasta_donde[0]
        self.hasta_donde = de_donde_hasta_donde[1]

        
        
    def mover(self,rectangulo):
        if self.eje == "y":
            for lados in rectangulo: 
                rectangulo[lados].y -= self.velocidad * self.orientacion_plataforma
            if rectangulo[lados].y < self.de_donde or rectangulo[lados].y > self.hasta_donde:    
                self.orientacion_plataforma = self.orientacion_plataforma * -1 
        elif self.eje == "x":
            for lados in rectangulo: 
                rectangulo[lados].x -= self.velocidad * self.orientacion_plataforma
            if rectangulo[lados].x < self.de_donde or rectangulo[lados].x > self.hasta_donde:    
                self.orientacion_plataforma = self.orientacion_plataforma * -1 
    
    def update(self,pantalla):
        self.mover(self.lados)
        pantalla.blit(self.imagen, self.rectangulo)
        
class Item:
    def __init__(self, tamaño, path):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen,(self.ancho,self.alto))
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = random.randrange(50,800,10)
        self.rectangulo.y = random.randrange(5,690,10)
        self.lados = obtener_rectangulo(self.rectangulo)
        self.orientacion_item = 1
        self.velocidad = 5
    
    def movimiento_y(self, rectangulo):
        for lados in rectangulo: 
            rectangulo[lados].y -= self.velocidad * self.orientacion_item
        if rectangulo[lados].y < 0 or rectangulo[lados].y > 700:    
            self.orientacion_item = self.orientacion_item * -1 
                    
    def update(self,pantalla):
        self.movimiento_y(self.lados)
        pantalla.blit(self.imagen, self.rectangulo)

class Objetivo:
    def __init__(self, tamaño, posicion,path):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen,(self.ancho,self.alto))
        self.rectangulo = self.imagen.get_rect()
        self.rectangulo.x = posicion[0]
        self.rectangulo.y = posicion[1]
        self.lados = obtener_rectangulo(self.rectangulo)
        
    def update(self,pantalla):
        pantalla.blit(self.imagen, self.rectangulo)

class PlataformaTrampa(Plataforma):
    def __init__(self, tamaño, path, posicion_inicial,daño):
        super().__init__(tamaño, path, posicion_inicial)
        self.daño = daño

class ProyectilEnemigo(Personaje):
    def __init__(self,tamaño,path,posx,posy,velocidad):
        self.imagen_proyectil = pygame.image.load(path)
        self.imagen_proyectil = pygame.transform.scale(self.imagen_proyectil,(30,30))
        self.rect = self.imagen_proyectil.get_rect()
        self.velocidad_disparo = velocidad
        self.rect.x = posx
        self.rect.y = posy
        self.lados = obtener_rectangulo(self.rect)
            
    def update(self,pantalla):
        self.rect.x -= self.velocidad_disparo
        pantalla.blit(self.imagen_proyectil,self.rect)

class Boss(Enemigo):
    def __init__(self,de_donde_hasta_donde,posicion_hitbox,hitbox_disparos,tamaño, animaciones, posicion_inicial,velocidad,pantalla):
        super().__init__(de_donde_hasta_donde,posicion_hitbox,tamaño, animaciones, posicion_inicial,velocidad,pantalla)
        self.vidas = 5
        self.x_hitbox_disparos = hitbox_disparos[0]
        self.y_hitbox_disparos = hitbox_disparos[1]
        self.hitbox_real = pygame.Rect(self.x_hitbox,self.y_hitbox,100,130)
        self.lados_hitbox = obtener_rectangulo(self.hitbox_real)
        self.hitbox_disparos = pygame.Rect(self.x_hitbox_disparos,self.y_hitbox_disparos,900,100)
        self.cadencia = 2000
        self.ultimo_disparo = pygame.time.get_ticks()
    
    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        
        if self.contador_de_pasos >= largo:
            self.contador_de_pasos = 0
            
        pantalla.blit(animacion[self.contador_de_pasos], self.lados["main"])
        self.contador_de_pasos += 1
        
        
    def mover(self,rectangulo,hitbox_real):
        for lado in rectangulo:
            rectangulo[lado].x += self.velocidad * self.orientacion_enemigo
        if rectangulo[lado].x > self.de_donde or rectangulo[lado].x < self.hasta_donde:
            self.orientacion_enemigo = self.orientacion_enemigo * -1
            self.de_donde = self.de_donde
            self.hasta_donde = self.hasta_donde
        for lado in hitbox_real:
            hitbox_real[lado].x += self.velocidad * self.orientacion_enemigo
        if hitbox_real[lado].x > self.de_donde + 40 or hitbox_real[lado].x < self.hasta_donde +60:
            self.orientacion_enemigo = self.orientacion_enemigo * -1
    
    def disparar(self):
        bala_enemigo = ProyectilEnemigo((30,30),"Enemigos\_SCML/3/a¬row.png",self.hitbox_real.x,self.hitbox_real.y+30,20)
        lista_enemigo_balas.append(bala_enemigo)
        lista_lados_enemigo_balas.append(bala_enemigo.lados)
    
    def verificar_colision_jugador(self,jugador,balas_jugador):
        for lados in jugador.lados:
            if self.lados_hitbox["right"].colliderect(jugador.lados["left"]) or self.lados_hitbox["left"].colliderect(jugador.lados["right"]):
                jugador.contador_vidas -= 1
                efectos_de_sonido("PC Computer - Star Wars Yoda Stories - Sound Effects\HURT.WAV")
            if jugador.contador_vidas < 1:
                jugador.desaparecer_personaje(jugador.lados)
            elif self.lados_hitbox["top"].colliderect(jugador.lados["bottom"]):
                self.vidas -= 1
                efectos_de_sonido("PC Computer - Dragon Ball FighterZ - Android 18\Android #18\Default/vaen109.ogg")

        for balas in balas_jugador:
            if self.lados_hitbox["left"].colliderect(balas.lados["main"]):
                efectos_de_sonido("PC Computer - Dragon Ball FighterZ - Android 18\Android #18\Default/vaen109.ogg")
                efectos_de_sonido("PC Computer - Dragon Ball FighterZ - Android 18\Android #18\Default/vaen030.ogg")
                self.vidas -= 1
                
        if self.vidas < 1:
            self.matar_boss()        
            
                
    def matar_boss(self):
        for lado in self.lados:
            self.lados[lado].x = -100000
            self.lados[lado].y = -100000
        for lado in self.lados_hitbox:
            self.lados_hitbox[lado].x = -100000
            self.lados_hitbox[lado].y = -100000
    
    def update(self, pantalla,jugador,balas_jugador):
        self.mover(self.lados,self.lados_hitbox)
        if self.orientacion_enemigo == 1:
            self.animar(pantalla, "camina_derecha")
        else:
            self.animar(pantalla, "camina_izquierda")
            
        if self.hitbox_disparos.colliderect(jugador.lados["main"]):
            tiempo = pygame.time.get_ticks()
            if tiempo - self.ultimo_disparo > self.cadencia:
                self.disparar()
                self.ultimo_disparo = tiempo
        
        self.verificar_colision_jugador(jugador,balas_jugador)
            
        
        
lista_balas = []
lista_lados_balas = []

lista_enemigo_balas = []
lista_lados_enemigo_balas = []

def efectos_de_sonido(sonido:str):
    pygame.mixer.init()
    sonido_colision = pygame.mixer.Sound(sonido)
    pygame.mixer.Sound.play(sonido_colision)
    


    
        
    
        

        
            
            
        
        
        
    
   
    
        
        
        
        
    
    
        



        
        
    
    