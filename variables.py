import pygame
import random
import time

pygame.init()
pygame.font.init()

############ variaveis globais ###############

global x

################# colors #####################

white = (255,255,255)
green = (0  , 150, 150)
orange = (255, 140, 0)
blue = (0, 0, 150)
black = (20, 20, 20)
yellow = (255,255,  0)
pink = (255,182,193)
greenForm = (120,211,55)
selectColor = (0, 255, 200)
beingClicked = (0, 200, 140)

##############################################

#compara cor e forma de 2 elementos diferentes (form.geoColor e form.geoForm)
def compare(form1, form2):
    if (form1.geoForm == form2.geoForm) and (form1.geoColor == form2.geoColor):
        return True
    else:
        return False

#define o ecra
screen = pygame.display.set_mode((1000, 600))
#fontes
myFont = pygame.font.Font(pygame.font.get_default_font(), 23)
lastClickedFont = pygame.font.Font(pygame.font.get_default_font(), 16)
victoryFont = pygame.font.Font(pygame.font.get_default_font(), 45)
#imagens
image = pygame.image.load("shuffle.png")
#songs
buttonSound = pygame.mixer.Sound("button sound.ogg")


    
            





