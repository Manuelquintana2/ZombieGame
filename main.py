import pygame

ANCHO = 900
ALTO = 700
ventana = (ANCHO,ALTO)
flag = True

pygame.init()

PANTALLA = pygame.display.set_mode((ventana))

#ICONO
icono = pygame.image.load("palanquita_mando.png")
pygame.display.set_icon((icono))

#FONDO_MENU
fondo = pygame.image.load("menu.jpg")
fondo_final = pygame.transform.scale(fondo, ventana)
PANTALLA.blit(fondo_final,(0,0))

#MUSICA
pygame.mixer.music.load("8 free sounds/burbuja.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.09)

while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
    
    pygame.display.update()
        



