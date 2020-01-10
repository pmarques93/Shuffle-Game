from button import *
from variables import *


#########################       menuScreen        #####################################

def menuScreen():
    global x
    #cria os botoes de texto 
    level1 = Text(450, 280, 100, 30)
    level2 = Text(450, 340, 100, 30)
    level3 = Text(450, 400, 100, 30)
    leave = Text(450, 500, 100, 30)
    
    x = 0
    while(x == 0):
        #limpa ecra, e coloca imagem
        screen.fill((20,20,20))
        screen.blit(image, (100, 0))
        #define variavel para quando o rato e pressed
        mb = pygame.mouse.get_pressed()
        pos_x, pos_y = pygame.mouse.get_pos()
        #desenha os botoes
        if level1.isAt (pos_x, pos_y):
            level1.draw(screen, selectColor, 1, '4x3')
        else:
            level1.draw(screen, yellow, 1, '4x3')
        if level2.isAt (pos_x, pos_y):
            level2.draw(screen, selectColor, 1, '4x4')
        else:
            level2.draw(screen, yellow, 1, '4x4')
        if level3.isAt (pos_x, pos_y):
            level3.draw(screen, selectColor, 1, '5x4')
        else:
            level3.draw(screen, yellow, 1, '5x4')
        if leave.isAt (pos_x, pos_y):
            leave.draw(screen, selectColor, 1, 'Exit')
        else:
            leave.draw(screen, yellow, 1, 'Exit')
        #quando os botoes são clicked
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            if (mb[0]):
                if level1.isAt(pos_x, pos_y):   #firstLevelScreen
                    x = 1
                if level2.isAt(pos_x, pos_y):  #secondLevelScreen
                    x = 2
                if level3.isAt(pos_x, pos_y):   #thirdLevelScreen
                    x = 3
                if leave.isAt(pos_x, pos_y):
                    exit()

        pygame.display.flip()

##########################       gamePlay        ######################################

def gamePlay():
    global x
    #varráveis para o score
    score = 0
    scoreCount = 0
    scoreFail = 0

    #tempCount serve para comparar a carta clicked com a última clicked
    tempCount = 0

    #helpBonus var
    helpBonus = False
    helpsLeft = 3

    if (x == 1):    # level1 formas e cards
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

        #lista para saber qual foi a última carta clicked
        allClicked = []

        #botão help
        helpCard = Text(875, 550, 105, 30)

        #cria botao leave
        leave = Text(20, 550, 100, 30)  

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
            card31, card32, card33, card34,
            ]

    if (x == 2):    # level2 formas e cards
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

        #lista para saber qual foi a última carta clicked
        allClicked = []

        #botão help
        helpCard = Text(875, 550, 105, 30)

        #cria botao leave
        leave = Text(20, 550, 100, 30)  

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

    if (x == 3):    # level3 formas e cards
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

        #lista para saber qual foi a última carta clicked
        allClicked = []

        #botão help
        helpCard = Text(875, 550, 105, 30)

        #cria botao leave
        leave = Text(20, 550, 100, 30)

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

    gameOn = True
    while(gameOn):
        screen.fill((20,20,20))
        #define variavel para quando o rato é pressed, define posicao x e y do rato
        mb = pygame.mouse.get_pressed()
        pos_x, pos_y = pygame.mouse.get_pos()

        #para todos os botoes que forem carregados
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            for card in cardList:
                if card.isAt(pos_x, pos_y):
                    if card.isClickable:
                        if mb[0]:
                            card.isClicked = True
                            card.isClickable = False
                            tempCount += 1  #para comparar clicked cards
                            allClicked.append(card)     #adiciona a lista para saber ultimo clickado
                            
                    else:
                        pass    #se ja foi clicked nao faz nada
            if leave.isAt(pos_x, pos_y):
                if mb[0]:
                    gameOn = False
                    x = 0
            if helpCard.isAt(pos_x, pos_y):
                if mb[0] and helpsLeft > 0:
                    helpBonus = True
                    helpsLeft -= 1


        ################### desenha exit button e score ###################
        leave.draw(screen, yellow, 1, 'Exit')   #desenha botao exit
        text = myFont.render("Score: " + str(score), True, yellow) #cria score
        screen.blit(text,(20,20))   #desenha score
        if leave.isAt(pos_x, pos_y):
            leave.draw(screen, selectColor, 1, 'Exit')
        ################### desenha exit button e score ###################

        ################### desenha a última forma clicked ###################
        if (len(allClicked)) > 0:
            lastClicked = lastClickedFont.render("- Last form clicked -", True, yellow)
            screen.blit(lastClicked,(20,250))
            pygame.draw.rect(screen, allClicked[-1].geoColor, (50, 275, 70, 70), 1)
            last = Card(0, 0, 0, 0)
            last.form(screen, allClicked[-1].geoForm, allClicked[-1].geoColor, 60, 285)
        ################### desenha a última forma clicked ###################

        ############################ help button ############################
        #desenha botao help quando rato ta por cima ou nao
        if helpCard.isAt(pos_x, pos_y):
            helpCard.draw(screen, selectColor, 1, 'help')
        else: 
            helpCard.draw(screen, yellow, 1, 'help') 
        helpLeft = myFont.render("Helps Left", True, yellow) #cria texto helps left
        helpLeftNum = myFont.render(str(helpsLeft), True, yellow) #cria texto helps left
        screen.blit(helpLeft,(870, 495))   #desenha helps left  
        screen.blit(helpLeftNum,(925, 522))   #desenha helps left     
        #botao help ao ser carregado
        if helpBonus:
            for card in cardList:
                card.draw(screen, black, 0)
                card.form(screen, card.geoForm, card.geoColor, card.x+xlen, card.y+ylen)
                pygame.display.flip()
                pygame.time.delay(150)
                helpBonus = False
        ############################ help button ############################

        #######################   score + victory    ########################
        #score nao pode ser negativo     
        if score < 0:
            score = 0
        #mensagem de vitoria
        if len(cardList) == 0:
            text = victoryFont.render("CONGRATULATIONS", True, yellow)
            risingScore = victoryFont.render("Score: " + str(score), True, yellow)
            screen.blit(risingScore, (380, 375))
            screen.blit(text,(270,275))
        #######################   score + victory    ########################

        ####################   desenha cartas formas    #####################
        for card in cardList:   #para todas as cartas na card list
            if card.isClicked == False:
                card.draw(screen, green, 0)  #se nao foi clickada desenha a carta
                if card.isAt(pos_x, pos_y):
                    card.draw(screen, selectColor, 0) # desenha carta com outra cor

            if card.isClicked == True:  # se carta ja foi selecionada
                card.form(screen, card.geoForm, card.geoColor, card.x+xlen, card.y+ylen) #desenha forma
                card.isClickable = False
        ####################   desenha cartas formas    #####################
        
        #################   compara as 2 cartas clicked    ##################
        if tempCount == 2:
            if compare(allClicked[-1], allClicked[-2]): #compara geo form e geocolor
                pygame.display.flip()
                pygame.time.delay(1000)
                for card in cardList:
                    if card.isClickable == False:   # para as cartas selecionadas na lista
                        cardList.remove(card)             

                score += 100    #adiciona 100 score, aumenta o score count
                scoreCount += 1        
                tempCount = 0
            else:
                pygame.display.flip()
                pygame.time.delay(1000)
                for card in cardList:   # se nao eram iguais, vai fazer "reset" às cartas
                    if card.isClickable == False:
                        card.isClicked = False
                        card.isClickable = True
                        ##se o jogador ja pontuou, tira +20 score cada erro, remove formas da clickedList
                if scoreCount > 0: # se ja pontuou antes
                    scoreFail += 20 # todas as vezes que falha perde +20
                    score -= scoreFail
                tempCount = 0       
        #################   compara as 2 cartas clicked    ##################        

        pygame.display.flip()

###########################       main        #########################################

def main ():
    global x
    menuScreen()
    while (True):

        if (x == 0):
            menuScreen()

        if (x > 0):
            gamePlay()

#######################################################################################

main()