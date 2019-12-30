import pygame
import random
from button import *
from variables import *


def menuScreen():
    global x
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))
    #define fonte
    myFont = pygame.font.SysFont('Arial', 23)
    image = pygame.image.load("shuffle.png")

    while(x == 0):
        #limpa ecra, e coloca image
        screen.fill((0,0,0))
        screen.blit(image, (100, 0))
        mb = pygame.mouse.get_pressed()

        #cria as cartas
        level1 = Text(450, 280, 100, 30)
        level1.draw(screen, yellow, white, 1, '4x3')
        level2 = Text(450, 340, 100, 30)
        level2.draw(screen, yellow, white, 1, '4x4')
        level3 = Text(450, 400, 100, 30)
        level3.draw(screen, yellow, white, 1, '5x4')
        leave = Text(450, 500, 100, 30)
        leave.draw(screen, yellow, white, 1, 'Exit')


        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            if (mb[0]):
                if (level1.pos):   #firstLevelScreen
                    x = 1
                if (leave.pos):
                    exit()

        pygame.display.flip()

#########################       firstLevel        #####################################

def firstLevel():
    global x
    #define resolucao de ecra e fonte
    screen = pygame.display.set_mode((1000, 600))
    myFont = pygame.font.SysFont('Arial', 23)
    score = 0
    xlen, ylen = 25, 50
    

    #####################    Formas e cores por trás das cartas  #####################
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

    # lista em que vão ser adicionadas clickedCards, que vai servir para  comparar se as cards são iguais
    clickedList = []
    

    while(x == 1):
        screen.fill((0,0,0))
        mb = pygame.mouse.get_pressed()
        pos_x, pos_y = pygame.mouse.get_pos()

        #cria as cartas
        card11 = Card(265, 50, 100, 150)
        card21 = Card(265, 225, 100, 150)
        card31 = Card(265, 400, 100, 150)
        card12 = Card(390, 50, 100, 150)
        card22 = Card(390, 225, 100, 150)
        card32 = Card(390, 400, 100, 150)
        card13 = Card(515, 50, 100, 150)
        card23 = Card(515, 225, 100, 150)
        card33 = Card(515, 400, 100, 150)
        card14 = Card(640, 50, 100, 150)
        card24 = Card(640, 225, 100, 150)
        card34 = Card(640, 400, 100, 150)


        #exit e score
        leave = Text(20, 550, 100, 30)
        leave.draw(screen, yellow, white, 1, 'Exit')
        text = myFont.render("Score: " + str(score), True, yellow)
        writeText = screen.blit(text,(20,20))

        #adiciona as cartas a uma lista
        cardList = [
            card11, card12, card13, card14,
            card21, card22, card23, card24,
            card31, card32, card33, card34
            ]

        #para todos os botoes que forem carregados
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()

            for card in cardList:
                if mb[0]:
                    if card.pos:
                        card.isClicked = True
                    if leave.pos:
                        x = 0


        #print das cards se nao forem clicked
        #ou adiciona a uma lista se forem clicked
        for card in cardList:
            if card.isClicked == False:
                card.draw(screen, green, white, 0)
            if card.isClicked == True:
                clickedList.append(card)


        #todas as cartas na lista de cartas clicked
        for card in clickedList:
            pygame.draw.rect(screen, black, (card.x, card.y, card.xlenght, card.ylenght,), 0)
            compareCount = len(clickedList)

            if compareCount == 2:
                if (compare(clickedList[0].form, clickedList[1].form)) == True:
                    score += 50
                    clickedList.pop()
                    clickedList.pop()
                else:
                    clickedList.pop()
                    clickedList.pop()



     
        
    
        pygame.display.flip()

###########################       main        #######################################

def main ():
    #pygame
    pygame.init()
    pygame.font.init()
    myFont = pygame.font.SysFont('Arial', 23)
    global x

    x = 0
    while (True):

        if (x == 0):
            menuScreen()

        if (x == 1):
            firstLevel()

#####################################################################################

main()