from button import *
from variables import *


#########################       menuScreen        #####################################

def menuScreen():
    global x
    global levelLock
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.load('menu song.ogg')
    pygame.mixer.music.play(-1)
    #cria os botoes de texto 
    level1 = Text(450, 280, 100, 30)
    level2 = Text(450, 320, 100, 30)
    level3 = Text(450, 360, 100, 30)
    level4 = Text(450, 400, 100, 30)
    level5 = Text(450, 440, 100, 30)
    unblock = Text(795, 550, 185, 30)
    leave = Text(450, 500, 100, 30)

    checkFirstLoop = 0 #so para detetar se é o primeiro loop do jogo
    
    while(x == 0):
        #limpa ecra, e coloca imagem
        screen.fill((20,20,20))
        #so vai executar este if primeira ve de cada codigo
        mb = pygame.mouse.get_pressed()

        if checkFirstLoop == 0:
            screen.blit(image, (100, 150))
            pygame.display.flip()
            time.sleep(3)
            for i in range(150):
                screen.blit(image, (100, 150-i))
                pygame.display.flip()
                screen.fill((20,20,20))
            checkFirstLoop += 1

        screen.blit(image, (100, 0))

        #define x e y do rato
        pos_x, pos_y = pygame.mouse.get_pos()
        #desenha os botoes
        if level1.isAt (pos_x, pos_y):
            level1.draw(screen, selectColor, 1, 'Level 1')
        else:
            level1.draw(screen, yellow, 1, 'Level 1')
        
        if levelLock > 1:
            level2.isClickable = True
            if level2.isAt (pos_x, pos_y):
                level2.draw(screen, selectColor, 1, 'Level 2')
            else:
                level2.draw(screen, yellow, 1, 'Level 2')
        else:
            level2.draw(screen, greenForm, 1, 'Level 2')
            level2.isClickable = False

        if levelLock > 2:
            level3.isClickable = True
            if level3.isAt (pos_x, pos_y):
                level3.draw(screen, selectColor, 1, 'Level 3')
            else:
                level3.draw(screen, yellow, 1, 'Level 3')  
        else:
            level3.draw(screen, greenForm, 1, 'Level 3')
            level3.isClickable = False

        if levelLock > 3:
            level4.isClickable = True
            if level4.isAt (pos_x, pos_y):
                level4.draw(screen, selectColor, 1, 'Level 4')
            else:
                level4.draw(screen, yellow, 1, 'Level 4')
        else:
            level4.draw(screen, greenForm, 1, 'Level 4')
            level4.isClickable = False

        if levelLock > 4:
            level5.isClickable = True
            if level5.isAt (pos_x, pos_y):
                level5.draw(screen, selectColor, 1, 'Level 5')
            else:
                level5.draw(screen, yellow, 1, 'Level 5')
        else:
            level5.draw(screen, greenForm, 1, 'Level 5')
            level5.isClickable = False

        if unblock.isAt (pos_x, pos_y):
            unblock.draw(screen, selectColor, 1, 'Unblock Levels')
        else:
            unblock.draw(screen, yellow, 1, 'Unblock Levels')
        if leave.isAt (pos_x, pos_y):
            leave.draw(screen, selectColor, 1, 'Exit')
        else:
            leave.draw(screen, yellow, 1, 'Exit')
        #quando os botoes são clicked
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if level1.isAt(pos_x, pos_y) and level1.isClickable:   #firstLevelScreen
                    x = 1
                if level2.isAt(pos_x, pos_y) and level2.isClickable:  #secondLevelScreen
                    x = 2
                if level3.isAt(pos_x, pos_y) and level3.isClickable:   #thirdLevelScreen
                    x = 3
                if level4.isAt(pos_x, pos_y) and level4.isClickable:   #forthLevelScreen
                    x = 4
                if level5.isAt(pos_x, pos_y) and level5.isClickable:   #fifthLevelScreen
                    x = 5
                if unblock.isAt(pos_x, pos_y):
                    levelLock = 5
                if leave.isAt(pos_x, pos_y):
                    exit()

        pygame.display.flip()

#####################       gamePlayEasyLevels       ##################################

def gamePlayEasyLevels():   # level 1 - 3
    global x, levelLock
    #varráveis para o score
    score = 0
    scoreCount = 0
    scoreFail = 0

    #tempCount serve para comparar a carta clicked com a última clicked
    tempCount = 0

    #helpBonus var
    helpBonus = False
    helpsLeft = 3

    #lista para saber qual foi a última carta clicked
    allClicked = []
    if len(allClicked) > 4: #vai limpando as cartas que ja não são precisas
        allClicked.pop(0)
        allClicked.pop(1)

    #botão help
    helpCard = Text(875, 550, 105, 30)

    #cria botao exit
    leave = Text(20, 550, 100, 30)  

    #cria bota nextLevel no fim
    nextLevel = Text(20, 500, 140, 30)

    if (x == 1):    #level 1 formas e cards
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.load('level 1 song.ogg')
        pygame.mixer.music.play(-1)
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
        Pos = [
            [265, 50], [390, 50], [515, 50], [640, 50],
            [265, 225], [390, 225], [515, 225], [640, 225],
            [265, 400], [390, 400], [515, 400], [640, 400],

        ]
        random.shuffle(Pos)
        ##################################################################################
        ##########################  cria as cartas e formas    ###########################
        card11 = Card(Pos[0][0], Pos[0][1], 100, 150)
        card11.form(screen, forms[0], colors[0], card11.x+xlen, card11.y+ylen)
        ##########
        card21 = Card(Pos[1][0], Pos[1][1], 100, 150)
        card21.form(screen, forms[1], colors[0], card21.x+xlen, card21.y+ylen)
        ##########
        card31 = Card(Pos[2][0], Pos[2][1], 100, 150)
        card31.form(screen, forms[2], colors[0], card31.x+xlen, card31.y+ylen)
        ##########
        card12 = Card(Pos[3][0], Pos[3][1], 100, 150)
        card12.form(screen, forms[3], colors[0], card12.x+xlen, card12.y+ylen)
        ##########
        card22 = Card(Pos[4][0], Pos[4][1], 100, 150)
        card22.form(screen, forms[4], colors[0], card22.x+xlen, card22.y+ylen)
        ##########
        card32 = Card(Pos[5][0], Pos[5][1], 100, 150)
        card32.form(screen, forms[5], colors[0], card32.x+xlen, card32.y+ylen)
        ##########
        card13 = Card(Pos[6][0], Pos[6][1], 100, 150)
        card13.form(screen, forms[0], colors[1], card13.x+xlen, card13.y+ylen)
        ##########
        card23 = Card(Pos[7][0], Pos[7][1], 100, 150)
        card23.form(screen, forms[1], colors[1], card23.x+xlen, card23.y+ylen)
        ##########
        card33 = Card(Pos[8][0], Pos[8][1], 100, 150)
        card33.form(screen, forms[2], colors[1], card33.x+xlen, card33.y+ylen)
        ##########
        card14 = Card(Pos[9][0], Pos[9][1], 100, 150)
        card14.form(screen, forms[3], colors[1], card14.x+xlen, card14.y+ylen)
        ##########
        card24 = Card(Pos[10][0],Pos[10][1], 100, 150)
        card24.form(screen, forms[4], colors[1], card24.x+xlen, card24.y+ylen)
        ##########
        card34 = Card(Pos[11][0],Pos[11][1], 100, 150)
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
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.load('level 2 song.ogg')
        pygame.mixer.music.play(-1)
        #variavel que define metade do tamanho das cartas
        xlen, ylen = 10, 30

        #####################    Formas e cores por trás das cartas  #####################
        #cria lista de formas e cores, faz random de modo a criar combinacoes diferentes
        forms = ['square', 'circle', 'square', 'circle']
        colors = [orange, blue, pink, greenForm]

        #faz shuffle das listas para criar diferentes combinacoes
        random.shuffle(colors)
        random.shuffle(forms)
        ##################################################################################
        Pos = [
            [330, 50], [420, 50], [510, 50], [600, 50],
            [330, 180], [420, 180], [510, 180], [600, 180],
            [330, 310], [420, 310], [510, 310], [600, 310],
            [330, 440], [420, 440], [510, 440], [600, 440],
        ]
        random.shuffle(Pos)
        ##################################################################################
        ##########################  cria as cartas e formas    ###########################
        card11 = Card(Pos[0][0], Pos[0][1], 70, 110)
        card11.form(screen, forms[0], colors[0], card11.x+xlen, card11.y+ylen)
        ##########
        card21 = Card(Pos[1][0], Pos[1][1], 70, 110)
        card21.form(screen, forms[1], colors[0], card21.x+xlen, card21.y+ylen)
        ##########
        card31 = Card(Pos[2][0], Pos[2][1], 70, 110)
        card31.form(screen, forms[2], colors[0], card31.x+xlen, card31.y+ylen)
        ##########
        card41 = Card(Pos[3][0], Pos[3][1], 70, 110)
        card41.form(screen, forms[3], colors[0], card41.x+xlen, card41.y+ylen)
        ##########
        card12 = Card(Pos[4][0], Pos[4][1], 70, 110)
        card12.form(screen, forms[0], colors[1], card12.x+xlen, card12.y+ylen)
        ##########
        card22 = Card(Pos[5][0], Pos[5][1], 70, 110)
        card22.form(screen, forms[1], colors[1], card22.x+xlen, card22.y+ylen)
        ##########
        card32 = Card(Pos[6][0], Pos[6][1], 70, 110)
        card32.form(screen, forms[2], colors[1], card32.x+xlen, card32.y+ylen)
        ##########
        card42 = Card(Pos[7][0], Pos[7][1], 70, 110)
        card42.form(screen, forms[3], colors[1], card42.x+xlen, card42.y+ylen)
        ##########
        card13 = Card(Pos[8][0], Pos[8][1], 70, 110)
        card13.form(screen, forms[0], colors[2], card13.x+xlen, card13.y+ylen)
        ##########
        card23 = Card(Pos[9][0], Pos[9][1], 70, 110)
        card23.form(screen, forms[1], colors[2], card23.x+xlen, card23.y+ylen)
        ##########
        card33 = Card(Pos[10][0], Pos[10][1], 70, 110)
        card33.form(screen, forms[2], colors[2], card33.x+xlen, card33.y+ylen)
        ##########
        card43 = Card(Pos[11][0], Pos[11][1], 70, 110)
        card43.form(screen, forms[3], colors[2], card43.x+xlen, card43.y+ylen)
        ##########
        card14 = Card(Pos[12][0], Pos[12][1], 70, 110)
        card14.form(screen, forms[0], colors[3], card14.x+xlen, card14.y+ylen)
        ##########
        card24 = Card(Pos[13][0], Pos[13][1], 70, 110)
        card24.form(screen, forms[1], colors[3], card24.x+xlen, card24.y+ylen)
        ##########
        card34 = Card(Pos[14][0], Pos[14][1], 70, 110)
        card34.form(screen, forms[2], colors[3], card34.x+xlen, card34.y+ylen)
        ##########
        card44 = Card(Pos[15][0], Pos[15][1], 70, 110)
        card44.form(screen, forms[3], colors[3], card44.x+xlen, card44.y+ylen)
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
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load('level 3 song.ogg')
        pygame.mixer.music.play(-1)
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
        pos_x, pos_y = pygame.mouse.get_pos()

        ########################### clicks do rato ##########################
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            for card in cardList:
                if card.isAt(pos_x, pos_y):
                    if card.isClickable:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            card.beingClicked = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            buttonSound.play()
                            card.isClicked = True
                            card.isClickable = False
                            tempCount += 1  #para comparar clicked cards
                            allClicked.append(card)     #adiciona a lista para saber ultimo clickado
                            
                    else:
                        pass    #se ja foi clicked nao faz nada
            if leave.isAt(pos_x, pos_y):
                if event.type == pygame.MOUSEBUTTONUP:
                    gameOn = False
                    x = 0
            if helpCard.isAt(pos_x, pos_y):
                if event.type == pygame.MOUSEBUTTONUP and helpsLeft > 0:
                    helpBonus = True
                    helpsLeft -= 1
            if nextLevel.isAt(pos_x, pos_y):
                if event.type == pygame.MOUSEBUTTONUP:
                    x += 1
                    gameOn = False
                        
        ########################## clicks do rato ###########################
        
        ##################### desenha exit button e score ####################
        leave.draw(screen, yellow, 1, 'Exit')   #desenha botao exit
        text2 = myFont.render("Level: " + str(x), True, yellow) #cria lvl
        if score <= 0:
            text = myFont.render("Score: 0", True, yellow) #cria score
        else:
            text = myFont.render("Score: " + str(score), True, yellow) #cria score
        screen.blit(text,(20,20))   #desenha score
        screen.blit(text2,(20,50))   #desenha lvl
        if leave.isAt(pos_x, pos_y):
            leave.draw(screen, selectColor, 1, 'Exit')
        ##################### desenha exit button e score ####################

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

        ###########################    victory    ###########################
        #mensagem de vitoria
        if len(cardList) < 2:   #para confirmar se é mesmo o ultimo par escolhido
            for card in cardList:
                cardList.remove(card)
            text = victoryFont.render("CONGRATULATIONS", True, yellow) 
            risingScore = victoryFont.render("Score: " + str(score), True, yellow)
            screen.blit(risingScore, (380, 325))
            screen.blit(text,(270,275))
            if x == 1 and levelLock < 2:
                levelLock = 2
            if x == 2 and levelLock < 3:
                levelLock = 3
            if x == 3 and levelLock < 4:
                levelLock = 4
            if x > 0:
                if nextLevel.isAt(pos_x, pos_y):
                    nextLevel.draw(screen, selectColor, 1, 'Next Level')
                else:
                    nextLevel.draw(screen, yellow, 1, 'Next Level')
        ###########################    victory    ###########################

        ####################   desenha cartas formas    #####################
        for card in cardList:   #para todas as cartas na card list
            if card.isClicked == False:
                card.draw(screen, green, 0)  #se nao foi clickada desenha a carta
                if card.isAt(pos_x, pos_y):
                    card.draw(screen, selectColor, 0) # desenha carta com outra cor
                    if card.beingClicked:
                        card.draw(screen, beingClicked, 0)
                else:
                    card.beingClicked = False

            if card.isClicked:  # se carta ja foi selecionada
                card.form(screen, card.geoForm, card.geoColor, card.x+xlen, card.y+ylen) #desenha forma
                card.isClickable = False
        ####################   desenha cartas formas    #####################
        
        #################   compara as 2 cartas clicked    ##################
        #score nao pode ser negativo     
        if score < 0:
            score = 0
        if tempCount == 2:
            if compare(allClicked[-1], allClicked[-2]): #compara geo form e geocolor
                pygame.display.flip()
                pygame.time.delay(1000)
                for card in cardList:
                    if card == allClicked[-1] or card == allClicked[-2]: #se a carta for igual a umas das comparadas
                        cardList.remove(card)             
                score += 100    #adiciona 100 score, aumenta o score count
                scoreCount += 1        
                tempCount = 0
            else:
                pygame.display.flip()
                pygame.time.delay(1000)
                for card in cardList:   # se nao eram iguais, vai fazer "reset" às cartas
                    if card == allClicked[-1] or card == allClicked[-2]: #se a carta for igual a uma das cmparadas
                        card.isClicked = False
                        card.isClickable = True
                ##se o jogador ja pontuou, tira +20 score cada erro
                if scoreCount > 0: # se ja pontuou antes
                    scoreFail += 20 # todas as vezes que falha perde +20
                    score -= scoreFail
                tempCount = 0
        
        if tempCount == 0:  #corrige um bug em que as cartas por vezes nao eram removidas da lista
            for card in cardList:   #quando nao ha cartas selecionadas apaga as que estao viradas
                if card.isClicked or card.isClickable == False:
                    cardList.remove(card)
        #################   compara as 2 cartas clicked    ##################        

        pygame.display.flip()

#####################       gamePlayHardLevels       ##################################

def gamePlayHardLevels():   # level 4 - 5
    global x
    global levelLock
    #varráveis para o score
    score = 0
    scoreCount = 0
    scoreFail = 0

    #tempCount serve para comparar a carta clicked com a última clicked
    tempCount = 0

    #helpBonus var
    helpBonus = False
    helpsLeft = 2

    #lista para saber qual foi a última carta clicked
    allClicked = []
    if len(allClicked) > 4: #vai limpando as cartas que ja não são precisas
        allClicked.pop(0)
        allClicked.pop(1)

    #botão help
    helpCard = Text(875, 550, 105, 30)

    #cria botao exit
    leave = Text(20, 550, 100, 30)  

    #cria bota nextLevel no fim
    nextLevel = Text(20, 500, 140, 30)

    if (x == 4):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load('level 4 song.ogg')
        pygame.mixer.music.play(-1)

    if (x == 5):
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.load('level 5 song.ogg')
        pygame.mixer.music.play(-1)


    #variavel que define metade do tamanho das cartas
    xlen, ylen = 10, 25

    #####################    Formas e cores por trás das cartas  #####################
    #cria lista de formas e cores, faz random de modo a criar combinacoes diferentes
    forms = ['square', 'circle', 'triangle', 'square', 'circle', 'triangle']
    colors = [orange, blue, pink, greenForm, yellow]

    #faz shuffle das listas para criar diferentes combinacoes
    random.shuffle(colors)
    random.shuffle(forms)
    
    ##################################################################################
    #cria todas as posicoes possiveis e faz random
    Pos = [
            [270, 60], [350, 60], [430, 60], [510, 60], [590, 60], [670, 60],
            [270, 160], [350, 160], [430, 160], [510, 160], [590, 160], [670, 160],
            [270, 260], [350, 260], [430, 260], [510, 260], [590, 260], [670, 260],
            [270, 360], [350, 360], [430, 360], [510, 360], [590, 360], [670, 360],
            [270, 460], [350, 460], [430, 460], [510, 460], [590, 460], [670, 460],
        ]
    random.shuffle(Pos)
    ##################################################################################
    ##########################  cria as cartas e formas    ###########################
    card11 = Card(Pos[0][0], Pos[0][1], 60, 85)
    card11.smallForm(screen, forms[0], colors[0], card11.x+xlen, card11.y+ylen)
    ##########
    card21 = Card(Pos[1][0], Pos[1][1], 60, 85)
    card21.smallForm(screen, forms[1], colors[0], card21.x+xlen, card21.y+ylen)
    ##########
    card31 = Card(Pos[2][0], Pos[2][1], 60, 85)
    card31.smallForm(screen, forms[2], colors[0], card31.x+xlen, card31.y+ylen)
    ##########
    card41 = Card(Pos[3][0], Pos[3][1], 60, 85)
    card41.smallForm(screen, forms[3], colors[0], card41.x+xlen, card41.y+ylen)
    ##########
    card51 = Card(Pos[4][0], Pos[4][1], 60, 85)
    card51.smallForm(screen, forms[4], colors[0], card51.x+xlen, card51.y+ylen)
    ##########
    card12 = Card(Pos[5][0], Pos[5][1], 60, 85)
    card12.smallForm(screen, forms[5], colors[0], card12.x+xlen, card12.y+ylen)
    ##########
    card22 = Card(Pos[6][0], Pos[6][1], 60, 85)
    card22.smallForm(screen, forms[0], colors[1], card22.x+xlen, card22.y+ylen)
    ##########
    card32 = Card(Pos[7][0], Pos[7][1], 60, 85)
    card32.smallForm(screen, forms[1], colors[1], card32.x+xlen, card32.y+ylen)
    ##########
    card42 = Card(Pos[8][0], Pos[8][1], 60, 85)
    card42.smallForm(screen, forms[2], colors[1], card42.x+xlen, card42.y+ylen)
    ##########
    card52 = Card(Pos[9][0], Pos[9][1], 60, 85)    
    card52.smallForm(screen, forms[3], colors[1], card52.x+xlen, card52.y+ylen)
    ##########
    card13 = Card(Pos[10][0],Pos[10][1], 60, 85)
    card13.smallForm(screen, forms[4], colors[1], card13.x+xlen, card13.y+ylen)
    ##########
    card23 = Card(Pos[11][0],Pos[11][1], 60, 85)
    card23.smallForm(screen, forms[5], colors[1], card23.x+xlen, card23.y+ylen)
    ##########
    card33 = Card(Pos[12][0],Pos[12][1], 60, 85)
    card33.smallForm(screen, forms[0], colors[2], card33.x+xlen, card33.y+ylen)
    ##########
    card43 = Card(Pos[13][0],Pos[13][1], 60, 85)
    card43.smallForm(screen, forms[1], colors[2], card43.x+xlen, card43.y+ylen)
    ##########
    card53 = Card(Pos[14][0],Pos[14][1], 60, 85)    
    card53.smallForm(screen, forms[2], colors[2], card53.x+xlen, card53.y+ylen)
    ##########
    card14 = Card(Pos[15][0],Pos[15][1], 60, 85)
    card14.smallForm(screen, forms[3], colors[2], card14.x+xlen, card14.y+ylen)
    ##########
    card24 = Card(Pos[16][0],Pos[16][1], 60, 85)
    card24.smallForm(screen, forms[4], colors[2], card24.x+xlen, card24.y+ylen)
    ##########
    card34 = Card(Pos[17][0],Pos[17][1], 60, 85)
    card34.smallForm(screen, forms[5], colors[2], card34.x+xlen, card34.y+ylen)
    ##########
    card44 = Card(Pos[18][0],Pos[18][1], 60, 85)
    card44.smallForm(screen, forms[0], colors[3], card44.x+xlen, card44.y+ylen)
    ##########
    card54 = Card(Pos[19][0],Pos[19][1], 60, 85)    
    card54.smallForm(screen, forms[1], colors[3], card54.x+xlen, card54.y+ylen)
    ##########
    card15 = Card(Pos[20][0],Pos[20][1], 60, 85)
    card15.smallForm(screen, forms[2], colors[3], card15.x+xlen, card15.y+ylen)
    ##########
    card25 = Card(Pos[21][0],Pos[21][1], 60, 85)
    card25.smallForm(screen, forms[3], colors[3], card25.x+xlen, card25.y+ylen)
    ##########
    card35 = Card(Pos[22][0],Pos[22][1], 60, 85)
    card35.smallForm(screen, forms[4], colors[3], card35.x+xlen, card35.y+ylen)
    ##########
    card45 = Card(Pos[23][0],Pos[23][1], 60, 85)
    card45.smallForm(screen, forms[5], colors[3], card45.x+xlen, card45.y+ylen)
    ##########
    card55 = Card(Pos[24][0],Pos[24][1], 60, 85)    
    card55.smallForm(screen, forms[0], colors[4], card55.x+xlen, card55.y+ylen)
    ##########
    card16 = Card(Pos[25][0],Pos[25][1], 60, 85)
    card16.smallForm(screen, forms[1], colors[4], card16.x+xlen, card16.y+ylen)
    ##########
    card26 = Card(Pos[26][0],Pos[26][1], 60, 85)
    card26.smallForm(screen, forms[2], colors[4], card26.x+xlen, card26.y+ylen)
    ##########
    card36 = Card(Pos[27][0],Pos[27][1], 60, 85)
    card36.smallForm(screen, forms[3], colors[4], card36.x+xlen, card36.y+ylen)
    ##########
    card46 = Card(Pos[28][0],Pos[28][1], 60, 85)
    card46.smallForm(screen, forms[4], colors[4], card46.x+xlen, card46.y+ylen)
    ##########
    card56 = Card(Pos[29][0],Pos[29][1], 60, 85)    
    card56.smallForm(screen, forms[5], colors[4], card56.x+xlen, card56.y+ylen)
    ##################################################################################
    ##################################################################################
    #adiciona as cartas a uma lista
    cardList = [
        card11, card12, card13, card14, card15, card16,
        card21, card22, card23, card24, card25, card26,
        card31, card32, card33, card34, card35, card36,
        card41, card42, card43, card44, card45, card46,
        card51, card52, card53, card54, card55, card56,
        ]

    gameOn = True
    while(gameOn):
        screen.fill((20,20,20))
        #define variavel para quando o rato é pressed, define posicao x e y do rato
        pos_x, pos_y = pygame.mouse.get_pos()


        ########################### clicks do rato ##########################
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
            for card in cardList:
                if card.isAt(pos_x, pos_y):
                    if card.isClickable:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            card.beingClicked = True
                        if event.type == pygame.MOUSEBUTTONUP:
                            buttonSound.play()
                            card.isClicked = True
                            card.isClickable = False
                            tempCount += 1  #para comparar clicked cards
                            allClicked.append(card)     #adiciona a lista para saber ultimo clickado
                            
                    else:
                        pass    #se ja foi clicked nao faz nada
            if leave.isAt(pos_x, pos_y):
                if event.type == pygame.MOUSEBUTTONUP:
                    gameOn = False
                    x = 0
            if helpCard.isAt(pos_x, pos_y):
                if event.type == pygame.MOUSEBUTTONUP and helpsLeft > 0:
                    helpBonus = True
                    helpsLeft -= 1
            if nextLevel.isAt(pos_x, pos_y):
                if event.type == pygame.MOUSEBUTTONUP:
                    x += 1
                    gameOn = False
        ########################## clicks do rato ###########################
        
        ##################### desenha exit button e score ####################
        leave.draw(screen, yellow, 1, 'Exit')   #desenha botao exit
        text2 = myFont.render("Level: " + str(x), True, yellow) #cria lvl
        if score <= 0:
            text = myFont.render("Score: 0", True, yellow) #cria score
        else:
            text = myFont.render("Score: " + str(score), True, yellow) #cria score
        screen.blit(text,(20,20))   #desenha score
        screen.blit(text2,(20,50))   #desenha lvl
        if leave.isAt(pos_x, pos_y):
            leave.draw(screen, selectColor, 1, 'Exit')
        ##################### desenha exit button e score ####################

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
                card.smallForm(screen, card.geoForm, card.geoColor, card.x+xlen, card.y+ylen)
                pygame.display.flip()
                pygame.time.delay(50)
                helpBonus = False
        ############################ help button ############################

        ###########################    victory    ###########################
        #mensagem de vitoria
        if len(cardList) < 2:   #para confirmar se é mesmo o ultimo par escolhido
            for card in cardList:
                cardList.remove(card)
            text = victoryFont.render("CONGRATULATIONS", True, yellow) 
            risingScore = victoryFont.render("Score: " + str(score), True, yellow)
            screen.blit(risingScore, (380, 325))    #desenha score final
            screen.blit(text,(270,275))  
            if x == 4:      #desenha o botao para o prox lvl
                if nextLevel.isAt(pos_x, pos_y):
                    nextLevel.draw(screen, selectColor, 1, 'Next Level')
                else:
                    nextLevel.draw(screen, yellow, 1, 'Next Level')
                if levelLock < 5: 
                    levelLock = 5
        ###########################   victory    ############################


        ####################   desenha cartas formas    #####################
        for card in cardList:   #para todas as cartas na card list
            if card.isClicked == False:
                if x == 5:
                    #efeito para mexer as cartas
                    if card.y >= -100:
                        card.y += 1
                        if card.y > 600:
                            card.y = -100
                card.draw(screen, green, 0)  #se nao foi clickada desenha a carta
                if card.isAt(pos_x, pos_y):
                    card.draw(screen, selectColor, 0) # desenha carta com outra cor
                    if card.beingClicked:
                        card.draw(screen, beingClicked, 0)
                else:
                    card.beingClicked = False
        
            if card.isClicked:  # se carta ja foi selecionada
                card.smallForm(screen, card.geoForm, card.geoColor, card.x+xlen, card.y+ylen) #desenha forma
                card.isClickable = False
                #efeito para mexer as cartas
                if x == 5:                
                    if card.y >= -100:
                        card.y += 1
                        if card.y > 600:
                            card.y = -100

        ####################   desenha cartas formas    #####################
        
        #################   compara as 2 cartas clicked    ##################
        #score nao pode ser negativo     
        if score < 0:
            score = 0
        if tempCount == 2:
            if compare(allClicked[-1], allClicked[-2]): #compara geo form e geocolor
                pygame.display.flip()
                pygame.time.delay(250)
                for card in cardList:
                    if card == allClicked[-1] or card == allClicked[-2]: #se a carta for igual a umas das comparadas
                        cardList.remove(card)             
                score += 100    #adiciona 100 score, aumenta o score count
                scoreCount += 1        
                tempCount = 0
            else:
                pygame.display.flip()
                pygame.time.delay(250)
                for card in cardList:   # se nao eram iguais, vai fazer "reset" às cartas
                    if card == allClicked[-1] or card == allClicked[-2]: #se a carta for igual a uma das cmparadas
                        card.isClicked = False
                        card.isClickable = True
                ##se o jogador ja pontuou, tira +20 score cada erro
                if scoreCount > 0: # se ja pontuou antes
                    scoreFail += 20 # todas as vezes que falha perde +20
                    score -= scoreFail
                tempCount = 0
        
        if tempCount == 0:  #corrige um bug em que as cartas por vezes nao eram removidas da lista
            for card in cardList:   #quando nao ha cartas selecionadas apaga as que estao viradas
                if card.isClicked or card.isClickable == False:
                    cardList.remove(card)
        #################   compara as 2 cartas clicked    ##################        

        pygame.display.flip()

###########################       main        #########################################

def main ():
    global x
    global levelLock
    #menuScreen()
    x = 0
    levelLock = 1
    while (True):

        if (x == 0):
            menuScreen()

        if x > 0 and x < 4:
            gamePlayEasyLevels()
        
        if x > 3:
            gamePlayHardLevels()

#######################################################################################

main()