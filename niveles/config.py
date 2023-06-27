import pygame

def girar_imagenes(lista_original, flip_x: bool, flip_y: bool)-> list:
    lista_girada = []
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada

def reescalar_imagen(lista_animaciones, tamaño):
    for i in range(len(lista_animaciones)):
            lista_animaciones[i] = pygame.transform.scale(lista_animaciones[i], tamaño)

def obtener_rectangulo(principal: pygame.Rect)->dict:
    diccionario = {}
    #main - bottom - left - top - right
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 11, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 11 , principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 6)
    
    return diccionario



personaje_quieto = [
    pygame.image.load("Zombies/PNG/Zombie1/animation/Attack4.png"),
    pygame.image.load("Zombies/PNG/Zombie1/animation/Attack5.png")
#     pygame.image.load("Zombies/PNG/Zombie1/animation/Hurt3.png"),
#     pygame.image.load("Zombies/PNG/Zombie1/animation/Hurt4.png"),
#     pygame.image.load("Zombies/PNG/Zombie1/animation/Hurt5.png")
]

personaje_camina = [    
    # pygame.image.load("Zombies/PNG/Zombie1/animation/Run1.png"),
    # pygame.image.load("Zombies/PNG/Zombie1/animation/Run2.png"),
    # pygame.image.load("Zombies/PNG/Zombie1/animation/Run3.png"),
    pygame.image.load("Zombies/PNG/Zombie1/animation/Run4.png"),
    pygame.image.load("Zombies/PNG/Zombie1/animation/Run5.png"),
    pygame.image.load("Zombies/PNG/Zombie1/animation/Run6.png"),
    pygame.image.load("Zombies/PNG/Zombie1/animation/Run7.png"),
    pygame.image.load("Zombies/PNG/Zombie1/animation/Run8.png"),
    pygame.image.load("Zombies/PNG/Zombie1/animation/Run9.png"),
    pygame.image.load("Zombies/PNG/Zombie1/animation/Run10.png")
]

personaje_salta = [    
    # pygame.image.load("Zombies/PNG/Zombie1/animation/Jump1.png"),
    # pygame.image.load("Zombies/PNG/Zombie1/animation/Jump2.png"),
    # pygame.image.load("Zombies/PNG/Zombie1/animation/Jump3.png"),
    # pygame.image.load("Zombies/PNG/Zombie1/animation/Jump4.png"),
    pygame.image.load("Zombies/PNG/Zombie1/animation/Jump5.png")
    # pygame.image.load("Zombies/PNG/Zombie1/animation/Jump6.png"),
    # pygame.image.load("Zombies/PNG/Zombie1/animation/Jump7.png")
]


enemigo_derecha = [
    pygame.image.load("Enemigos/_PNG/1/Warrior_01__RUN_000.png"),
    pygame.image.load("Enemigos/_PNG/1/Warrior_01__RUN_001.png"),
    pygame.image.load("Enemigos/_PNG/1/Warrior_01__RUN_002.png"),
    pygame.image.load("Enemigos/_PNG/1/Warrior_01__RUN_003.png"),
    pygame.image.load("Enemigos/_PNG/1/Warrior_01__RUN_004.png"),
    pygame.image.load("Enemigos/_PNG/1/Warrior_01__RUN_005.png"),
    pygame.image.load("Enemigos/_PNG/1/Warrior_01__RUN_006.png"),
    pygame.image.load("Enemigos/_PNG/1/Warrior_01__RUN_007.png"),
    pygame.image.load("Enemigos/_PNG/1/Warrior_01__RUN_008.png"),
    pygame.image.load("Enemigos/_PNG/1/Warrior_01__RUN_009.png")
]

enemigo_cae = [pygame.image.load("Enemigos/_PNG/1/Warrior_01__JUMP_000.png"),
               pygame.image.load("Enemigos/_PNG/1/Warrior_01__JUMP_001.png"),
               pygame.image.load("Enemigos/_PNG/1/Warrior_01__JUMP_002.png"),
               pygame.image.load("Enemigos/_PNG/1/Warrior_01__JUMP_003.png"),
               pygame.image.load("Enemigos/_PNG/1/Warrior_01__JUMP_004.png"),
               pygame.image.load("Enemigos/_PNG/1/Warrior_01__JUMP_005.png"),
               pygame.image.load("Enemigos/_PNG/1/Warrior_01__JUMP_006.png"),
               pygame.image.load("Enemigos/_PNG/1/Warrior_01__JUMP_007.png"),
               pygame.image.load("Enemigos/_PNG/1/Warrior_01__JUMP_008.png"),
               pygame.image.load("Enemigos/_PNG/1/Warrior_01__JUMP_000.png")
]

enemigo_quieto = [pygame.image.load("Enemigos/_PNG/1/Warrior_01__HURT_000.png"),
                  pygame.image.load("Enemigos/_PNG/1/Warrior_01__HURT_001.png")   
]

enemigo_muere = [pygame.image.load("Enemigos/_PNG/1/Warrior_01__DIE_000.png"),
                 pygame.image.load("Enemigos/_PNG/1/Warrior_01__DIE_001.png"),
                 pygame.image.load("Enemigos/_PNG/1/Warrior_01__DIE_002.png"),
                 pygame.image.load("Enemigos/_PNG/1/Warrior_01__DIE_003.png"),
                 pygame.image.load("Enemigos/_PNG/1/Warrior_01__DIE_004.png"),
                 pygame.image.load("Enemigos/_PNG/1/Warrior_01__DIE_005.png"),
                 pygame.image.load("Enemigos/_PNG/1/Warrior_01__DIE_006.png"),
                 pygame.image.load("Enemigos/_PNG/1/Warrior_01__DIE_007.png"),
                 pygame.image.load("Enemigos/_PNG/1/Warrior_01__DIE_008.png"),
                 pygame.image.load("Enemigos/_PNG/1/Warrior_01__DIE_009.png")
]

enemigo_dos_derecha = [pygame.image.load("Enemigos\_PNG/2\Warrior_02__RUN_000.png"),
                       pygame.image.load("Enemigos\_PNG/2\Warrior_02__RUN_001.png"),
                       pygame.image.load("Enemigos\_PNG/2\Warrior_02__RUN_002.png"),
                       pygame.image.load("Enemigos\_PNG/2\Warrior_02__RUN_003.png"),
                       pygame.image.load("Enemigos\_PNG/2\Warrior_02__RUN_004.png"),
                       pygame.image.load("Enemigos\_PNG/2\Warrior_02__RUN_005.png"),
                       pygame.image.load("Enemigos\_PNG/2\Warrior_02__RUN_006.png"),
                       pygame.image.load("Enemigos\_PNG/2\Warrior_02__RUN_007.png"),
                       pygame.image.load("Enemigos\_PNG/2\Warrior_02__RUN_008.png"),
                       pygame.image.load("Enemigos\_PNG/2\Warrior_02__RUN_009.png"),]


enemigo_tres_derecha = [pygame.image.load("Enemigos\_PNG/3\Warrior_03__RUN_000.png"),
                        pygame.image.load("Enemigos\_PNG/3\Warrior_03__RUN_001.png"),
                        pygame.image.load("Enemigos\_PNG/3\Warrior_03__RUN_002.png"),
                        pygame.image.load("Enemigos\_PNG/3\Warrior_03__RUN_003.png"),
                        pygame.image.load("Enemigos\_PNG/3\Warrior_03__RUN_004.png"),
                        pygame.image.load("Enemigos\_PNG/3\Warrior_03__RUN_005.png"),
                        pygame.image.load("Enemigos\_PNG/3\Warrior_03__RUN_006.png"),
                        pygame.image.load("Enemigos\_PNG/3\Warrior_03__RUN_007.png"),
                        pygame.image.load("Enemigos\_PNG/3\Warrior_03__RUN_008.png"),
                        pygame.image.load("Enemigos\_PNG/3\Warrior_03__RUN_009.png")]

personaje_disparar = [pygame.image.load("Zombies\PNG\Zombie1/animation\Attack1.png"),
                      pygame.image.load("Zombies\PNG\Zombie1/animation\Attack2.png"),
                      pygame.image.load("Zombies\PNG\Zombie1/animation\Attack3.png"),
                      pygame.image.load("Zombies\PNG\Zombie1/animation\Attack4.png"),
                      pygame.image.load("Zombies\PNG\Zombie1/animation\Attack5.png"),
                      pygame.image.load("Zombies\PNG\Zombie1/animation\Attack6.png")]


personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)
enemigo_izquierda = girar_imagenes(enemigo_derecha,True,False)

enemigo_dos_izquierda = girar_imagenes(enemigo_dos_derecha,True,False)

enemigo_tres_izquierda = girar_imagenes(enemigo_tres_derecha,True,False)