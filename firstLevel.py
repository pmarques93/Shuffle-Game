import pygame
from button import *
from variables import *
import random


def firstLevel():
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))
    myFont = pygame.font.SysFont('Arial', 23)
    global x, white , orange, yellow, blue, xlen, ylen
    global isClicked
    isClicked = False

    #cria lista de formas e cores, faz random de modo a criar combinacoes diferentes
    forms = ['square', 'triangle', 'circle', 'square', 'triangle', 'circle']
    colors = [orange, blue]

    #faz shuffle das listas para criar diferentes combinacoes
    random.shuffle(colors)
    random.shuffle(forms)

    comboColors = []
    comboForms = []

    for i in colors:
        comboColors.append(i)
    for i in forms:
        comboForms.append(i)


    while(True):

        pos_x, pos_y = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            
            if (mb[0]):
                if (rectExit.pos):
                    #menuScreen
                    x = 0
                    print(x)



        
        #cria, desenha e define a posicao do rectangulo
        #aplica a classe geoForm(self, forms, colors, x, y, pos))
        rect11 = button(True, green, white, 365, 265, 50, 200, 265, 50, 100, 150, '')
        form11 = geoForm(comboForms[5], comboColors[0], rect11.x+xlen, rect11.y+ylen, rect11.pos) 
        #######
        rect21 = button(True, green, white, 365, 265, 225, 375, 265, 225, 100, 150, '')
        form21 = geoForm(comboForms[2], comboColors[0], rect21.x+xlen, rect21.y+ylen, rect21.pos)
        #######
        rect31 = button(True, green, white, 365, 265, 400, 550, 265, 400, 100, 150, '')
        form31 = geoForm(comboForms[5], comboColors[1], rect31.x+xlen, rect31.y+ylen, rect31.pos) 
        #######
        rect12 = button(True, green, white, 490, 390, 50, 200, 390, 50, 100, 150, '')
        form12 = geoForm(comboForms[0], comboColors[1], rect12.x+xlen, rect12.y+ylen, rect12.pos) 
        #######
        rect22 = button(True, green, white, 490, 390, 225, 375, 390, 225, 100, 150, '')
        form22 = geoForm(comboForms[1], comboColors[0], rect22.x+xlen, rect22.y+ylen, rect22.pos) 
        #######
        rect32 = button(True, green, white, 490, 390, 400, 550, 390, 400, 100, 150, '')
        form32 = geoForm(comboForms[4], comboColors[1], rect32.x+xlen, rect32.y+ylen, rect32.pos) 
        #######
        rect13 = button(True, green, white, 615, 515, 50, 200, 515, 50, 100, 150, '')
        form13 = geoForm(comboForms[2], comboColors[1], rect13.x+xlen, rect13.y+ylen, rect13.pos) 
        #######
        rect23 = button(True, green, white, 615, 515, 225, 375, 515, 225, 100, 150, '')
        form23 = geoForm(comboForms[4], comboColors[0], rect23.x+xlen, rect23.y+ylen, rect23.pos) 
        #######
        rect33 = button(True, green, white, 615, 515, 400, 550, 515, 400, 100, 150, '')
        form33 = geoForm(comboForms[3], comboColors[0], rect33.x+xlen, rect33.y+ylen, rect33.pos) 
        #######
        rect14 = button(True, green, white, 740, 640, 50, 200, 640, 50, 100, 150, '')
        form14 = geoForm(comboForms[0], comboColors[0], rect14.x+xlen, rect14.y+ylen, rect14.pos) 
        #######
        rect24 = button(True, green, white, 740, 640, 225, 375, 640, 225, 100, 150, '')
        form24 = geoForm(comboForms[3], comboColors[1], rect24.x+xlen, rect24.y+ylen, rect24.pos) 
        #######
        rect34 = button(True, green, white, 740, 640, 400, 550, 640, 400, 100, 150, '')
        form34 = geoForm(comboForms[1], comboColors[1], rect34.x+xlen, rect34.y+ylen, rect34.pos) 
        #######
        rectExit = button(False, yellow, white, 120, 20, 550, 580, 20, 550, 100, 30, 'Exit')
    


        
        

        pygame.display.flip()