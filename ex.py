import pygame
import random
import time
from button import *
from variables import *

#compara cor e forma de 2 elementos diferentes
def compare(form1, form2):
    if (form1.geoForm == form2.geoForm) and (form1.geoColor == form2.geoColor):
        return True
    else:
        return False


#########################       menuScreen        #####################################

def menuScreen():
    global x
    #define resolucao de ecra
    screen = pygame.display.set_mode((1000, 600))
    #define fonte
    myFont = pygame.font.Font(pygame.font.get_default_font(), 23)
    image = pygame.image.load("shuffle.png")

    while(x == 0):
        #limpa ecra, e coloca imagem
        screen.fill((20,20,20))
        screen.blit(image, (100, 0))
        #define variavel para quando o rato e pressed
        mb = pygame.mouse.get_pressed()

        #cria e desenha os botoes de texto 
        level1 = Text(450, 280, 100, 30)
        level1.draw(screen, yellow, 1, '4x3')
        level2 = Text(450, 340, 100, 30)
        level2.draw(screen, yellow, 1, '4x4')
        level3 = Text(450, 400, 100, 30)
        level3.draw(screen, yellow, 1, '5x4')
        leave = Text(450, 500, 100, 30)
        leave.draw(screen, yellow, 1, 'Exit')

        #quando os botoes são clicked
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            if (mb[0]):
                if (level1.pos):   #firstLevelScreen
                    x = 1
                if (level2.pos):   #secondLevelScreen
                    x = 2
                if (level3.pos):   #thirdLevelScreen
                    x = 3
                if (leave.pos):
                    exit()

        pygame.display.flip()

#########################       firstLevel        #####################################

def firstLevel():
    global x
    #define resolucao de ecra e cria fontes
    screen = pygame.display.set_mode((1000, 600))
    myFont = pygame.font.Font(pygame.font.get_default_font(), 23)
    lastClickedFont = pygame.font.Font(pygame.font.get_default_font(), 16)
    victoryFont = pygame.font.Font(pygame.font.get_default_font(), 45)

    #varráveis para o score
    score = 0
    scoreCount = 0
    scoreFail = 0

    #tempCount serve para comparar a carta clicked com a última clicked
    tempCount = 0

    #helpBonus var
    helpBonus = False

    #variavel que define metade do tamanho das cartas
    xlen, ylen = 25, 50

    #####################    Formas e cores por trás das cartas  #####################
    #cria lista de formas e cores, faz random de modo a criar combinacoes diferentes
    forms = ['square', 'triangle', 'circle', 'square', 'triangle', 'circle']
    colors = [orange, blue]

    #faz shuffle das listas para criar diferentes combinacoes
    random.shuffle(colors)
    random.shuffle(forms)
    ##################################################################################

    #lista em que vão ser adicionadas clickedCards, que vai servir para  comparar se as cards são iguais
    clickedList = []

    #lista para saber qual foi a última carta clicked
    allClicked = []

    #botão help
    helpCard = Text(880, 550, 105, 30)

    ##################################################################################
    ##########################  cria as cartas e formas    ###########################
    card11 = Card(265, 50, 100, 150)
    card11.form(screen, forms[5], colors[0], card11.x+xlen, card11.y+ylen)
    ##########
    card21 = Card(265, 225, 100, 150)
    card21.form(screen, forms[2], colors[0], card21.x+xlen, card21.y+ylen)
    ##########
    card31 = Card(265, 400, 100, 150)
    card31.form(screen, forms[0], colors[1], card31.x+xlen, card31.y+ylen)
    ##########
    card12 = Card(390, 50, 100, 150)
    card12.form(screen, forms[3], colors[1], card12.x+xlen, card12.y+ylen)
    ##########
    card22 = Card(390, 225, 100, 150)
    card22.form(screen, forms[0], colors[0], card22.x+xlen, card22.y+ylen)
    ##########
    card32 = Card(390, 400, 100, 150)
    card32.form(screen, forms[4], colors[0], card32.x+xlen, card32.y+ylen)
    ##########
    card13 = Card(515, 50, 100, 150)
    card13.form(screen, forms[1], colors[1], card13.x+xlen, card13.y+ylen)
    ##########
    card23 = Card(515, 225, 100, 150)
    card23.form(screen, forms[4], colors[1], card23.x+xlen, card23.y+ylen)
    ##########
    card33 = Card(515, 400, 100, 150)
    card33.form(screen, forms[3], colors[0], card33.x+xlen, card33.y+ylen)
    ##########
    card14 = Card(640, 50, 100, 150)
    card14.form(screen, forms[1], colors[0], card14.x+xlen, card14.y+ylen)
    ##########
    card24 = Card(640, 225, 100, 150)
    card24.form(screen, forms[2], colors[1], card24.x+xlen, card24.y+ylen)
    ##########
    card34 = Card(640, 400, 100, 150)
    card34.form(screen, forms[5], colors[1], card34.x+xlen, card34.y+ylen)
    ##################################################################################
    ##################################################################################

    #adiciona as cartas a uma lista
    cardList = [
        card11, card12, card13, card14,
        card21, card22, card23, card24,
        card31, card32, card33, card34
        ]

    while(x == 1):
        screen.fill((20,20,20))
        #define variavel para quando o rato é pressed, define posicao x e y do rato
        mb = pygame.mouse.get_pressed()
        pos_x, pos_y = pygame.mouse.get_pos()

        ################### desenha exit button e score ###################
        leave = Text(20, 550, 100, 30)  #cria botao leave
        leave.draw(screen, yellow, 1, 'Exit')   #desenha
        text = myFont.render("Score: " + str(score), True, yellow)  #cria score
        screen.blit(text,(20,20))   #desenha
        if leave.isAt(pos_x, pos_y):
            leave.draw(screen, selectColor, 1, 'Exit')
        ################### desenha exit button e score ###################

        ################### desenha a última forma clicked ###################
        if (len(allClicked)) > 0:
            lastClicked = lastClickedFont.render("- Last form clicked -", True, yellow)
            screen.blit(lastClicked,(20,250))
            pygame.draw.rect(screen, allClicked[-1].geoColor, (50, 275, 70, 70), 1)
            card.form(screen, allClicked[-1].geoForm, allClicked[-1].geoColor, 60, 285)
        ################### desenha a última forma clicked ###################

        ############################ help button ############################
        #desenha botao help quando rato ta por cima ou nao
        if helpCard.isAt(pos_x, pos_y):
            helpCard.draw(screen, selectColor, 1, 'Show All')
        else: 
            helpCard.draw(screen, yellow, 1, 'Show All')     
        #botao help ao ser carregado
        if helpBonus:
            screen.fill((20, 20, 20))    
            for card in cardList:
                card.form(screen, card.geoForm, card.geoColor, card.x+xlen, card.y+ylen)
                pygame.display.flip()
                pygame.time.delay(175)
                helpBonus = False
        ############################ help button ############################

        #######################   score + victory    ########################
        #score nao pode ser negativo     
        if score < 0:
            score = 0
        '''
        #mensagem de vitoria
        if len(tempList) == len(cardList):
            text = victoryFont.render("CONGRATULATIONS", True, yellow)
            screen.blit(text,(270,275))
        '''
        #######################   score + victory    ########################

        ####################   desenha cartas formas    #####################
        for card in cardList:   #para todas as cartas na clicked list
            if card.isClicked == False: #se nao foi clickada
                #card.draw(screen, green, 0)  #se nao foi clickada desenha a carta
                card.form(screen, card.geoForm, card.geoColor, card.x+xlen, card.y+ylen) #desenha forma

                if card.isAt(pos_x, pos_y): #se rato tiver por cima
                    card.draw(screen, selectColor, 0) # desenha carta de branco

            if card.isClicked == True:  # se carta ja foi selecionada for true
                card.form(screen, card.geoForm, card.geoColor, card.x+xlen, card.y+ylen) #desenha forma
                card.isClickable = False
                pass
        ####################   desenha cartas formas    #####################
        
        #################   compara as 2 cartas clicked    ##################
        if tempCount % 2 == 0 and tempCount != 0: #se tempcount for par ( selecionadas de 2 em 2)
            if compare(allClicked[-1], allClicked[-2]):
                for card in cardList:
                    if card.isClickable == False:
                        cardList.remove(card)
            else:
                for card in cardList:
                    if card.isClickable == False:
                        card.isClicked = False
                        card.isClickable = True
        #################   compara as 2 cartas clicked    ##################        


        #para todos os botoes que forem carregados
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            for card in cardList:   #para clickar nas cartas
                if card.isAt(pos_x, pos_y):     # se tiver na posicao da carta
                    if card.isClickable:
                        if mb[0]:   #se clickar
                            card.isClicked = True
                            card.isClickable = False
                            tempCount += 1
                            allClicked.append(card)     #adiciona a lista para saber ultimo clickado
                            #clickedList.append(card)    #adiciona a lista para ser comparado
                    else:
                        pass
            if leave.isAt(pos_x, pos_y):
                if mb[0]:
                    x = 0
            if helpCard.isAt(pos_x, pos_y):
                if mb[0]:
                    helpBonus = True   
                                   



        '''
        #todas as cartas na lista de cartas clicked
        for card in clickedList:
            #desenha forma
            card.form(screen, clickedList[0].geoForm, clickedList[0].geoColor, clickedList[0].x+xlen, clickedList[0].y+ylen)

            compareCount = len(clickedList)
            if compareCount == 2:

                
                #sao comparadas com a função compare()           
                if (compare(clickedList[0], clickedList[1])):

                    #espera 1500ms and mostra o resultado
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    #adiciona 100 score, aumenta o score count, remove formas da clickedList
                    score += 100
                    scoreCount += 1

                    

                    ##############
                    #remove da lista de cartas clickadas
                    clickedList.pop()
                    clickedList.pop()

                    
                else:
                    #espera 1500ms and mostra o resultado
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    ##se o jogador ja pontuou, tira +20 score cada erro, remove formas da clickedList
                    if scoreCount > 0:
                        scoreFail += 20
                        score -= scoreFail
                    clickedList.pop()
                    clickedList.pop()
        '''

        pygame.display.flip()

########################       secondLevel        #####################################

def secondLevel():
    global x
    #define resolucao de ecra e cria fontes
    screen = pygame.display.set_mode((1000, 600))
    myFont = pygame.font.Font(pygame.font.get_default_font(), 23)
    lastClickedFont = pygame.font.Font(pygame.font.get_default_font(), 16)
    victoryFont = pygame.font.Font(pygame.font.get_default_font(), 45)

    #varráveis para o score
    score = 0
    scoreCount = 0
    scoreFail = 0

    #helpBonus var
    helpBonus = False

    #variavel que define metade do tamanho das cartas
    xlen, ylen = 10, 30

    #####################    Formas e cores por trás das cartas  #####################
    #cria lista de formas e cores, faz random de modo a criar combinacoes diferentes
    forms = ['square', 'triangle', 'circle', 'square', 'triangle', 'circle']
    forms2 = ['square', 'triangle']
    colors = [orange, blue, pink]

    #faz shuffle das listas para criar diferentes combinacoes
    random.shuffle(colors)
    random.shuffle(forms)
    random.shuffle(forms2)
    ##################################################################################

    #lista em que vão ser adicionadas clickedCards, que vai servir para  comparar se as cards são iguais
    clickedList = []

    #lista para saber qual foi a última carta clicked
    allClicked = []
    
    #templist
    tempList = []

    while(x == 2):
        screen.fill((20,20,20))
        #define variavel para quando o rato é pressed, define posicao x e y do rato
        mb = pygame.mouse.get_pressed()
        pos_x, pos_y = pygame.mouse.get_pos()

        ##################################################################################
        ##########################  cria as cartas e formas    ###########################
        card11 = Card(330, 50, 70, 110)
        card11.form(screen, forms[5], colors[0], card11.x+xlen, card11.y+ylen)
        ##########
        card21 = Card(330, 180, 70, 110)
        card21.form(screen, forms[2], colors[0], card21.x+xlen, card21.y+ylen)
        ##########
        card31 = Card(330, 310, 70, 110)
        card31.form(screen, forms[0], colors[1], card31.x+xlen, card31.y+ylen)
        ##########
        card41 = Card(330, 440, 70, 110)
        card41.form(screen, forms2[0], colors[2], card41.x+xlen, card41.y+ylen)
        ##########
        card12 = Card(420, 50, 70, 110)
        card12.form(screen, forms[3], colors[1], card12.x+xlen, card12.y+ylen)
        ##########
        card22 = Card(420, 180, 70, 110)
        card22.form(screen, forms[0], colors[0], card22.x+xlen, card22.y+ylen)
        ##########
        card32 = Card(420, 310, 70, 110)
        card32.form(screen, forms2[1], colors[2], card32.x+xlen, card32.y+ylen)
        ##########
        card42 = Card(420, 440, 70, 110)
        card42.form(screen, forms[4], colors[0], card42.x+xlen, card42.y+ylen)
        ##########
        card13 = Card(510, 50, 70, 110)
        card13.form(screen, forms[1], colors[1], card13.x+xlen, card13.y+ylen)
        ##########
        card23 = Card(510, 180, 70, 110)
        card23.form(screen, forms[4], colors[1], card23.x+xlen, card23.y+ylen)
        ##########
        card33 = Card(510, 310, 70, 110)
        card33.form(screen, forms[3], colors[0], card33.x+xlen, card33.y+ylen)
        ##########
        card43 = Card(510, 440, 70, 110)
        card43.form(screen, forms2[1], colors[2], card43.x+xlen, card43.y+ylen)
        ##########
        card14 = Card(600, 50, 70, 110)
        card14.form(screen, forms[1], colors[0], card14.x+xlen, card14.y+ylen)
        ##########
        card24 = Card(600, 180, 70, 110)
        card24.form(screen, forms[2], colors[1], card24.x+xlen, card24.y+ylen)
        ##########
        card34 = Card(600, 310, 70, 110)
        card34.form(screen, forms2[0], colors[2], card34.x+xlen, card34.y+ylen)
        ##########
        card44 = Card(600, 440, 70, 110)
        card44.form(screen, forms[5], colors[1], card44.x+xlen, card44.y+ylen)
        ##################################################################################
        ##################################################################################

        #adiciona as cartas a uma lista
        cardList = [
            card11, card12, card13, card14,
            card21, card22, card23, card24,
            card31, card32, card33, card34,
            card41, card42, card43, card44
            ]

        #print do exit e score
        leave = Text(20, 550, 100, 30)
        leave.draw(screen, yellow, white, 1, 'Exit')
        text = myFont.render("Score: " + str(score), True, yellow)
        screen.blit(text,(20,20))

        #desenha a ultima forma clicked
        if (len(allClicked)) > 0:
            lastClicked = lastClickedFont.render("- Last form clicked -", True, yellow)
            screen.blit(lastClicked,(20,250))
            pygame.draw.rect(screen, allClicked[-1].geoColor, (50, 275, 70, 70), 1)
            card.form(screen, allClicked[-1].geoForm, allClicked[-1].geoColor, 60, 285)

        #botão help
        helpCard = Text(880, 550, 105, 30)
        helpCard.draw(screen, yellow, white, 1, 'Show All')

        #para todos os botoes que forem carregados
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            for card in cardList:
                if mb[0]:
                    if card.pos:
                        card.isClicked = True
                        pygame.time.delay(25)
                    if leave.pos:
                        x = 0
                    if helpCard.pos:
                        helpBonus = True
                        
                
        if helpBonus:
            for card in cardList:
                card.draw(screen, black, black, 0)
                card.form(screen, card.geoForm, card.geoColor, card.x+xlen, card.y+ylen)
                pygame.display.flip()
                pygame.time.delay(100)
                helpBonus = False
                

        #print das cards se nao forem clicked
        #ou adiciona a uma lista se forem clicked
        for card in cardList:
         
            if card.isClicked == False:
                card.draw(screen, green, white, 0)
            if card.isClicked == True:
                clickedList.append(card)
                allClicked.append(card)
        

        #todas as cartas na lista de cartas clicked
        for card in clickedList:
            #sao pintadas de preto
            #desenha forma por cima
            card.draw(screen, black, black, 0)
            card.form(screen, clickedList[0].geoForm, clickedList[0].geoColor, clickedList[0].x+xlen, clickedList[0].y+ylen)

            compareCount = len(clickedList)
            if compareCount == 2:
                #tempList pinta que ja foram escolhidas de preto
                for card in tempList:
                    card.draw(screen, black, black, 0)
                
                #sao comparadas com a função compare()           
                if (compare(clickedList[0], clickedList[1])):
                    #espera 1500ms and mostra o resultado
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    #adiciona 100 score, aumenta o score count, remove formas da clickedList
                    score += 100
                    scoreCount += 1

                   
                    #tempList
                    tempList.append(clickedList[0])
                    tempList.append(clickedList[1])
                    ###############################
                   

                    clickedList.pop()
                    clickedList.pop()
                else:
                    #espera 1500ms and mostra o resultado
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    ##se o jogador ja pontuou, tira +20 score cada erro, remove formas da clickedList
                    if scoreCount > 0:
                        scoreFail += 20
                        score -= scoreFail
                    clickedList.pop()
                    clickedList.pop()
        
        #score nao pode ser negativo     
        if score < 0:
            score = 0
        
        #tempList Teste
        tempL = len(tempList)
        if tempL >= 2:
            for card in tempList:
                card.draw(screen, black, black, 0)

        #mensagem de vitoria
        if len(tempList) == len(cardList):
            text = victoryFont.render("CONGRATULATIONS", True, yellow)
            screen.blit(text,(270,275))
       

        pygame.display.flip()

########################       thirdLevel        #####################################

def thirdLevel():
    global x
    #define resolucao de ecra e cria fontes
    screen = pygame.display.set_mode((1000, 600))
    myFont = pygame.font.Font(pygame.font.get_default_font(), 23)
    lastClickedFont = pygame.font.Font(pygame.font.get_default_font(), 16)
    victoryFont = pygame.font.Font(pygame.font.get_default_font(), 45)

    #varráveis para o score
    score = 0
    scoreCount = 0
    scoreFail = 0

    #helpBonus var
    helpBonus = False

    #variavel que define metade do tamanho das cartas
    xlen, ylen = 10, 30

    #####################    Formas e cores por trás das cartas  #####################
    #cria lista de formas e cores, faz random de modo a criar combinacoes diferentes
    forms = ['square', 'triangle', 'square', 'triangle']
    colors = [orange, blue, pink, greenForm, yellow]

    #faz shuffle das listas para criar diferentes combinacoes
    random.shuffle(colors)
    random.shuffle(forms)
    ##################################################################################

    #lista em que vão ser adicionadas clickedCards, que vai servir para  comparar se as cards são iguais
    clickedList = []

    #lista para saber qual foi a última carta clicked
    allClicked = []
    
    #templist
    tempList = []

    while(x == 3):
        screen.fill((20,20,20))
        #define variavel para quando o rato é pressed, define posicao x e y do rato
        mb = pygame.mouse.get_pressed()
        pos_x, pos_y = pygame.mouse.get_pos()

        ##################################################################################
        ##########################  cria as cartas e formas    ###########################
        card11 = Card(280, 50, 70, 110)
        card11.form(screen, forms[0], colors[4], card11.x+xlen, card11.y+ylen)
        ##########
        card21 = Card(280, 180, 70, 110)
        card21.form(screen, forms[2], colors[2], card21.x+xlen, card21.y+ylen)
        ##########
        card31 = Card(280, 310, 70, 110)
        card31.form(screen, forms[2], colors[4], card31.x+xlen, card31.y+ylen)
        ##########
        card41 = Card(280, 440, 70, 110)
        card41.form(screen, forms[3], colors[3], card41.x+xlen, card41.y+ylen)
        ##########
        card12 = Card(370, 50, 70, 110)
        card12.form(screen, forms[3], colors[0], card12.x+xlen, card12.y+ylen)
        ##########
        card22 = Card(370, 180, 70, 110)
        card22.form(screen, forms[2], colors[0], card22.x+xlen, card22.y+ylen)
        ##########
        card32 = Card(370, 310, 70, 110)
        card32.form(screen, forms[3], colors[4], card32.x+xlen, card32.y+ylen)
        ##########
        card42 = Card(370, 440, 70, 110)
        card42.form(screen, forms[1], colors[2], card42.x+xlen, card42.y+ylen)
        ##########
        card13 = Card(460, 50, 70, 110)
        card13.form(screen, forms[2], colors[1], card13.x+xlen, card13.y+ylen)
        ##########
        card23 = Card(460, 180, 70, 110)
        card23.form(screen, forms[0], colors[0], card23.x+xlen, card23.y+ylen)
        ##########
        card33 = Card(460, 310, 70, 110)
        card33.form(screen, forms[0], colors[2], card33.x+xlen, card33.y+ylen)
        ##########
        card43 = Card(460, 440, 70, 110)
        card43.form(screen, forms[2], colors[3], card43.x+xlen, card43.y+ylen)
        ##########
        card14 = Card(550, 50, 70, 110)
        card14.form(screen, forms[1], colors[0], card14.x+xlen, card14.y+ylen)
        ##########
        card24 = Card(550, 180, 70, 110)
        card24.form(screen, forms[0], colors[1], card24.x+xlen, card24.y+ylen)
        ##########
        card34 = Card(550, 310, 70, 110)
        card34.form(screen, forms[1], colors[3], card34.x+xlen, card34.y+ylen)
        ##########
        card44 = Card(550, 440, 70, 110)
        card44.form(screen, forms[3], colors[1], card44.x+xlen, card44.y+ylen)
        ##########
        card15 = Card(640, 50, 70, 110)
        card15.form(screen, forms[0], colors[3], card15.x+xlen, card15.y+ylen)
        ##########
        card25 = Card(640, 180, 70, 110)
        card25.form(screen, forms[1], colors[4], card25.x+xlen, card25.y+ylen)
        ##########
        card35 = Card(640, 310, 70, 110)
        card35.form(screen, forms[3], colors[2], card35.x+xlen, card35.y+ylen)
        ##########
        card45 = Card(640, 440, 70, 110)
        card45.form(screen, forms[1], colors[1], card45.x+xlen, card45.y+ylen)
        ##################################################################################
        ##################################################################################

        #adiciona as cartas a uma lista
        cardList = [
            card11, card12, card13, card14, card15,
            card21, card22, card23, card24, card25,
            card31, card32, card33, card34, card35,
            card41, card42, card43, card44, card45
            ]

        #print do exit e score
        leave = Text(20, 550, 100, 30)
        leave.draw(screen, yellow, white, 1, 'Exit')
        text = myFont.render("Score: " + str(score), True, yellow)
        screen.blit(text,(20,20))

        #desenha a ultima forma clicked
        if (len(allClicked)) > 0:
            lastClicked = lastClickedFont.render("- Last form clicked -", True, yellow)
            screen.blit(lastClicked,(20,250))
            pygame.draw.rect(screen, allClicked[-1].geoColor, (50, 275, 70, 70), 1)
            card.form(screen, allClicked[-1].geoForm, allClicked[-1].geoColor, 60, 285)

        #botão help
        helpCard = Text(880, 550, 105, 30)
        helpCard.draw(screen, yellow, white, 1, 'Show All')

        #para todos os botoes que forem carregados
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            for card in cardList:
                if mb[0]:
                    if card.pos:
                        card.isClicked = True
                        pygame.time.delay(25)
                    if leave.pos:
                        x = 0
                    if helpCard.pos:
                        helpBonus = True
                        
                
        if helpBonus:
            for card in cardList:
                card.draw(screen, black, black, 0)
                card.form(screen, card.geoForm, card.geoColor, card.x+xlen, card.y+ylen)
                pygame.display.flip()
                pygame.time.delay(200)
                helpBonus = False
                

        #print das cards se nao forem clicked
        #ou adiciona a uma lista se forem clicked
        for card in cardList:
         
            if card.isClicked == False:
                card.draw(screen, green, white, 0)
            if card.isClicked == True:
                clickedList.append(card)
                allClicked.append(card)
        

        #todas as cartas na lista de cartas clicked
        for card in clickedList:
            #sao pintadas de preto
            #desenha forma por cima
            card.draw(screen, black, black, 0)
            card.form(screen, clickedList[0].geoForm, clickedList[0].geoColor, clickedList[0].x+xlen, clickedList[0].y+ylen)

            compareCount = len(clickedList)
            if compareCount == 2:
                #tempList pinta que ja foram escolhidas de preto
                for card in tempList:
                    card.draw(screen, black, black, 0)
                
                #sao comparadas com a função compare()           
                if (compare(clickedList[0], clickedList[1])):
                    #espera 1500ms and mostra o resultado
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    #adiciona 100 score, aumenta o score count, remove formas da clickedList
                    score += 100
                    scoreCount += 1

                   
                    #tempList
                    tempList.append(clickedList[0])
                    tempList.append(clickedList[1])
                    ###############################
                   

                    clickedList.pop()
                    clickedList.pop()
                else:
                    #espera 1500ms and mostra o resultado
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    ##se o jogador ja pontuou, tira +20 score cada erro, remove formas da clickedList
                    if scoreCount > 0:
                        scoreFail += 20
                        score -= scoreFail
                    clickedList.pop()
                    clickedList.pop()
        
        #score nao pode ser negativo     
        if score < 0:
            score = 0
        
        #tempList Teste
        tempL = len(tempList)
        if tempL >= 2:
            for card in tempList:
                card.draw(screen, black, black, 0)

        #mensagem de vitoria
        if len(tempList) == len(cardList):
            text = victoryFont.render("CONGRATULATIONS", True, yellow)
            screen.blit(text,(270,275))
       

        pygame.display.flip()

###########################       main        #########################################

def main ():
    #pygame
    pygame.init()
    pygame.font.init()
    myFont = pygame.font.Font(pygame.font.get_default_font(), 23)
    global x

    x = 0
    while (True):

        if (x == 0):
            menuScreen()

        if (x == 1):
            firstLevel()

        if (x == 2):
            secondLevel()

        if (x ==3):
            thirdLevel()

#######################################################################################

main()