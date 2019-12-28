import pygame
import random
from button import *
from variables import *


#####################################################################################

def menuScreen():
    global x
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))
    #define font pygame.font
    myFont = pygame.font.SysFont('Arial', 23)
    #load da imagem
    image = pygame.image.load("shuffle.png")

    
    while(x == 0):
        
        #pinta o ecra todo com preto
        screen.fill((0,0,0))
        screen.blit(image, (100, 0))

        mb = pygame.mouse.get_pressed()
        
        # class button = color, colorOver, maxX, minX, minY, maxY, x, y, xlenght, ylenght, textInput   #
        #cria os rectangulos
        rect1 = button(False, yellow, white, 550, 450, 240, 270, 450, 240, 100, 30, '4x3')
        rect2 = button(False, yellow, white, 550, 450, 280, 310, 450, 280, 100, 30, '4x4')
        rect3 = button(False, yellow, white, 550, 450, 320, 350, 450, 320, 100, 30, '5x4')
        rect4 = button(False, yellow, white, 550, 450, 360, 390, 450, 360, 100, 30, '6x5')
        rect5 = button(False, yellow, white, 550, 450, 400, 430, 450, 400, 100, 30, '6x6')
        rectExit = button(False, yellow, white, 550, 450, 460, 490, 450, 460, 100, 30, 'Exit')
        

        #fecha o jogo quando se carregar no X
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            
            if (mb[0]):
                if (rect1.pos):   #firstLevelScreen
                    x = 1
            if (mb[0]):
                if (rect2.pos):
                    pass
            if (mb[0]):
                if (rect3.pos):
                    pass
            if (mb[0]):
                if (rect4.pos):
                    pass
            if (mb[0]):
                if (rect5.pos):
                    pass
            if (mb[0]):
                if (rectExit.pos):
                    exit()

        pygame.display.flip()

#########################       firstLevel       ####################################

def firstLevel():
    global x
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))
    myFont = pygame.font.SysFont('Arial', 23)
    score = 0

    ############    Formas e cores por trás das cartas  ############
    #cria lista de formas e cores, faz random de modo a criar combinacoes diferentes
    forms = ['square', 'triangle', 'circle', 'square', 'triangle', 'circle']
    colors = [orange, blue]

    #faz shuffle das listas para criar diferentes combinacoes
    random.shuffle(colors)
    random.shuffle(forms)

    #cria listas vazias
    comboColors = []
    comboForms = []

    #adiciona as combinacoes (shuffled) às novas listas
    for i in colors:
        comboColors.append(i)
    for i in forms:
        comboForms.append(i)
    ################################################################

    #dicionario (False se a carta nao foi clicked / True se a carta foi clicked)
    tempDict = {
        "temp11": False,    "temp12": False,    "temp13": False,    "temp14": False,
                                                 
        "temp21": False,    "temp22": False,    "temp23": False,    "temp24": False,
                                                                  
        "temp31": False,    "temp32": False,    "temp33": False,    "temp34": False,
    }


    while(x == 1):
        #adquire posição do rato
        #cria variavel para se o rotao for clicked
        pos_x, pos_y = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()
        screen.fill((0,0,0))


        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            # se clicar nas varias cartas
            if (mb[0]):
                if (rectExit.pos):
                    x = 0
                if (rect11.pos):
                    tempDict["temp11"] = True
                if (rect21.pos):  
                    tempDict["temp21"] = True
                if (rect31.pos):
                    tempDict["temp31"] = True
                if (rect12.pos):
                    tempDict["temp12"] = True
                if (rect22.pos):
                    tempDict["temp22"] = True
                if (rect32.pos):
                    tempDict["temp32"] = True
                if (rect13.pos):
                    tempDict["temp13"] = True
                if (rect23.pos):
                    tempDict["temp23"] = True
                if (rect33.pos):
                    tempDict["temp33"] = True
                if (rect14.pos):
                    tempDict["temp14"] = True
                if (rect24.pos):
                    tempDict["temp24"] = True
                if (rect34.pos):
                    tempDict["temp34"] = True


        rectExit = button(False, yellow, white, 120, 20, 550, 580, 20, 550, 100, 30, 'Exit')
        #score - desenha o score e atualiza#
        text = myFont.render("Score: " + str(score), True, yellow)
        writeText = screen.blit(text,(20,20))

        ######################  criacao das várias cartas  ######################
        #se nao for clickado, cria, desenha e define a posicao da carta  ### " rectYX " ###
        if (tempDict["temp11"]):
            #se for carregado pinta a carta de preto
            rect11 = button(True, black, black, 365, 265, 50, 200, 265, 50, 100, 150, '')
            #e aplica a classe que cria as formas - geoForm(self, forms, colors, x, y, pos)) ### " formYX " ###
            form11 = geoForm(comboForms[5], comboColors[0], rect11.x+xlen, rect11.y+ylen, rect11.pos) 
        else:
            rect11 = button(True, green, white, 365, 265, 50, 200, 265, 50, 100, 150, '')
        #######    
        if (tempDict["temp21"]):
            rect21 = button(True, black, black, 365, 265, 225, 375, 265, 225, 100, 150, '')
            form21 = geoForm(comboForms[2], comboColors[0], rect21.x+xlen, rect21.y+ylen, rect21.pos)
        else:
            rect21 = button(True, green, white, 365, 265, 225, 375, 265, 225, 100, 150, '')
        #######
        if (tempDict["temp31"]):
            rect31 = button(True, black, black, 365, 265, 400, 550, 265, 400, 100, 150, '')
            form31 = geoForm(comboForms[5], comboColors[1], rect31.x+xlen, rect31.y+ylen, rect31.pos) 
        else:
            rect31 = button(True, green, white, 365, 265, 400, 550, 265, 400, 100, 150, '')
        #######
        if (tempDict["temp12"]):
            rect12 = button(True, black, black, 490, 390, 50, 200, 390, 50, 100, 150, '')
            form12 = geoForm(comboForms[0], comboColors[1], rect12.x+xlen, rect12.y+ylen, rect12.pos) 
        else:
            rect12 = button(True, green, white, 490, 390, 50, 200, 390, 50, 100, 150, '')
        #######
        if (tempDict["temp22"]):
            rect22 = button(True, black, black, 490, 390, 225, 375, 390, 225, 100, 150, '')
            form22 = geoForm(comboForms[1], comboColors[0], rect22.x+xlen, rect22.y+ylen, rect22.pos)
        else:
            rect22 = button(True, green, white, 490, 390, 225, 375, 390, 225, 100, 150, '')
        ####### 
        if (tempDict["temp32"]):
            rect32 = button(True, black, black, 490, 390, 400, 550, 390, 400, 100, 150, '')
            form32 = geoForm(comboForms[4], comboColors[1], rect32.x+xlen, rect32.y+ylen, rect32.pos) 
        else:
            rect32 = button(True, green, white, 490, 390, 400, 550, 390, 400, 100, 150, '')
        #######
        if (tempDict["temp13"]):
            rect13 = button(True, black, black, 615, 515, 50, 200, 515, 50, 100, 150, '')
            form13 = geoForm(comboForms[2], comboColors[1], rect13.x+xlen, rect13.y+ylen, rect13.pos) 
        else:
            rect13 = button(True, green, white, 615, 515, 50, 200, 515, 50, 100, 150, '')
        #######
        if (tempDict["temp23"]):
            rect23 = button(True, black, black, 615, 515, 225, 375, 515, 225, 100, 150, '')
            form23 = geoForm(comboForms[4], comboColors[0], rect23.x+xlen, rect23.y+ylen, rect23.pos) 
        else:
            rect23 = button(True, green, white, 615, 515, 225, 375, 515, 225, 100, 150, '')   
        #######
        if (tempDict["temp33"]):
            rect33 = button(True, black, black, 615, 515, 400, 550, 515, 400, 100, 150, '')
            form33 = geoForm(comboForms[3], comboColors[0], rect33.x+xlen, rect33.y+ylen, rect33.pos)
        else:
            rect33 = button(True, green, white, 615, 515, 400, 550, 515, 400, 100, 150, '')
        #######
        if (tempDict["temp14"]):
            rect14 = button(True, black, black, 740, 640, 50, 200, 640, 50, 100, 150, '')
            form14 = geoForm(comboForms[0], comboColors[0], rect14.x+xlen, rect14.y+ylen, rect14.pos) 
        else:
            rect14 = button(True, green, white, 740, 640, 50, 200, 640, 50, 100, 150, '')
        #######
        if (tempDict["temp24"]):
            rect24 = button(True, black, black, 740, 640, 225, 375, 640, 225, 100, 150, '')
            form24 = geoForm(comboForms[3], comboColors[1], rect24.x+xlen, rect24.y+ylen, rect24.pos) 
        else:
            rect24 = button(True, green, white, 740, 640, 225, 375, 640, 225, 100, 150, '')
        #######
        if (tempDict["temp34"]):
            rect34 = button(True, black, black, 740, 640, 400, 550, 640, 400, 100, 150, '')
            form34 = geoForm(comboForms[1], comboColors[1], rect34.x+xlen, rect34.y+ylen, rect34.pos) 
        else:
            rect34 = button(True, green, white, 740, 640, 400, 550, 640, 400, 100, 150, '')
        #######
        
        ############     quando as cartas sáo clicked mete variavel isClicked = True      ############
        
        if (tempDict["temp11"]):
            rect11.isClicked = True
            lista.append(rect11)
        if (tempDict["temp21"]):
            rect21.isClicked = True
        if (tempDict["temp31"]):
            rect31.isClicked = True
        if (tempDict["temp12"]):
            rect12.isClicked = True
        if (tempDict["temp22"]):
            rect22.isClicked = True
        if (tempDict["temp32"]):
            rect32.isClicked = True
        if (tempDict["temp13"]):
            rect13.isClicked = True
        if (tempDict["temp23"]):
            rect23.isClicked = True
        if (tempDict["temp33"]):
            rect33.isClicked = True
        if (tempDict["temp14"]):
            rect14.isClicked = True
        if (tempDict["temp24"]):
            rect24.isClicked = True
        if (tempDict["temp34"]):
            rect34.isClicked = True
        

        ###################     compara se as cartas clicked são iguais ou nao      ###################

    

            
            


        '''
        #### compara rectangulos carregados ####
        if (tempDict["temp11"] == True) and (tempDict["temp21"] == True):
            if (compare(form11, form21) == True):
                rect11 = button(True, black, black, 365, 265, 50, 200, 265, 50, 100, 150, '')
                rect21 = button(True, black, black, 365, 265, 225, 375, 265, 225, 100, 150, '')
            if (compare(form11, form21) == False):
                tempDict["temp11"] = False
                tempDict["temp21"] = False
        '''
        



        pygame.display.flip()

###########################       main        #######################################

def main ():
    #pygame
    pygame.init()
    pygame.font.init()
    global x, yellow, white, green, black, pos_x, pos_y, screen, myFont

    x = 0
    while (True):

        if (x == 0):
            menuScreen()

        if (x == 1):
            firstLevel()

#####################################################################################



main()
