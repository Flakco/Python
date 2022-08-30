import math
from tkinter import font
from trace import Trace
import pygame
import random
from pygame import mixer


# ejecutar pygame
pygame.init()

# crea la pantalla
Screen = pygame.display.set_mode((800, 600))

# fondo
fondo = pygame.image.load("33.png")

# musica
mixer.music.load("DueloftheFates.mp3")
mixer.music.play(-1)


# cambiar el nombre y el logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-ship.png")
pygame.display.set_icon(icon)

# jugador
jugadorimg = pygame.image.load("battleship.png")
playerx = 370
playery = 500
playerx_change = 0

# enemigo
enemigoimg = []
enemix = []
enemiy = []
enemix_change = []
enemiy_change = []
numenemis = 5

for i in range(numenemis):
    enemigoimg.append(pygame.image.load("aircraft.png"))
    enemix.append(random.randint(3,736))
    enemiy.append(random.randint(0,100))
    enemix_change.append(0.1)
    enemiy_change.append(10)

# disparo
disparoimg = pygame.image.load("shot1.png")
disparox = 0
disparoy = 500
disparox_change = 0
disparoy_change = 0.3
disparo_estado = "ready"

# score
score = 0
font = pygame.font.Font("freesansbold.ttf",11)
textx = 740
texty = 575

overfont = pygame.font.Font("freesansbold.ttf",66)

def showscore(x,y):
    scored = font.render("Score: " + str(score), Trace, (222,222,222))
    Screen.blit(scored, (x, y))


def jugador(x, y):
    Screen.blit(jugadorimg, (x, y))

def enemigo(x, y, i):
    Screen.blit(enemigoimg[i], (x, y))

def disparo(x, y):
    global disparo_estado
    disparo_estado = "fire"
    Screen.blit(disparoimg,(x ,y - 30))

def iscollision(enemix, enemiy, disparox, disparoy):
    distance = math.sqrt((math.pow(enemix - disparox,2)) + (math.pow(enemiy - disparoy,2)))
    if distance < 40:
        return True
    else:
        return False

def gameover():
    over = overfont.render("GAME OVER", True, (222,222,222))
    Screen.blit(over, (200, 250))



# game loop
running = True
while running:
    # RGB - Red, Green, Blue
    Screen.fill((111, 0, 0))
    # fondo
    Screen.blit(fondo,(0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # que tecla se esta apretando, izquierda o derecha
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerx_change = -0.3
        if event.key == pygame.K_RIGHT:
            playerx_change = 0.3
        if event.key == pygame.K_UP:
            if disparo_estado == "ready":
                bdisparo = mixer.Sound("stard.mp3")
                bdisparo.play()
                disparox = playerx + 25
                disparo(disparox, disparoy)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerx_change = 0
               
         
    playerx += playerx_change

    if playerx <3:
        playerx = 3
    elif playerx >= 733:
        playerx = 733

    for i in range(numenemis):

        # game over
        if enemiy[i] > 200:
             for j in range(numenemis):
                 enemiy[i] = 2000
             gameover()
             break

        enemix[i] += enemix_change[i]
        if enemix[i] <=3:
            enemix_change[i] = 0.1
            enemiy[i] += enemiy_change[i]
        elif enemix[i] >= 733:
            enemix_change[i] = -0.1
            enemiy[i] += enemiy_change[i]

        # golpe
        collision = iscollision(enemix[i], enemiy[i], disparox, disparoy)
        if collision:
            ex = mixer.Sound("explo.mp3")
            ex.play()
            disparoy = 500
            disparo_estado = "ready"
            score += 100
            print(score)
            enemix[i] = random.randint(3,736)
            enemiy[i] = random.randint(0,100)

        enemigo(enemix[i], enemiy[i], i)

    # disparo movimiento
    if disparoy <= 0:
        disparoy = 500
        disparo_estado = "ready"

    if disparo_estado == "fire":
        disparo(disparox, disparoy)
        disparoy -= disparoy_change
    
    
    showscore(textx, texty)
    jugador(playerx, playery)
    pygame.display.update()
    
