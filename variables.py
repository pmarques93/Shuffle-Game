import pygame

pygame.init()
pygame.font.init()

############ variaveis globais ###############

global x, z, pos_x, pos_y, screen, myFont, mb

mb = pygame.mouse.get_pressed()
pos_x, pos_y = pygame.mouse.get_pos()

################# colors #####################

global black, white, yellow, green, orange, pink, blue
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,  0)
green = (0  , 150, 0)
orange = (255, 140, 0)
pink = (199,21,133)
blue = (0, 0, 150)

##############################################

screen = pygame.display.set_mode((1000, 600))
myFont = pygame.font.SysFont('Arial', 23)

########## variaveis firstLevel ##############

global xlen, ylen
xlen, ylen = 25, 50

##############################################
#funcoes temp

def compare(sq1, sq2):
    if (sq1 == sq2):
        print ("test compare")


def twoClicks(sq1, sq2):
    firstClick = False
    secondClick = False

    if (sq1.pos):
        if (mb[0]):
            firstClick = True
            





