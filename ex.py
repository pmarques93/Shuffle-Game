import pygame
from button import *
from variables import *
from firstLevel import *


##############################################################################
def menuScreen():
    global x
    #define font pygame.font
    myFont = pygame.font.SysFont('Arial', 23)
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))
    #load da imagem
    image = pygame.image.load("shuffle.png")
    


    while(x == 0):
        #cria a posição do rato para x e y
        pos_x, pos_y = pygame.mouse.get_pos()
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
##############################################################################


##############################################################################
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
##############################################################################
main()
