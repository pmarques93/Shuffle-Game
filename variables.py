import pygame

pygame.init()
pygame.font.init()

#variaveis globais
global x, z, black, yellow, white, green, orange, pink, blue, pos_x, pos_y, screen, myFont
black, yellow, white, green, orange, pink, blue = (0,0,0), (255,255,  0), (255,255,255), (0  , 150, 0), (255, 140, 0), (199,21,133), (0, 0, 150)
screen = pygame.display.set_mode((1000, 600))
myFont = pygame.font.SysFont('Arial', 23)
#variaveis firstLevel
global xlen, ylen
xlen, ylen = 25, 50








