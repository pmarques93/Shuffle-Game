import pygame
from variables import *

class button:

    def __init__ (self, card, color, colorOver, maxX, minX, minY, maxY, x, y, xlenght, ylenght, textInput):
        pos_x, pos_y = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()
        
        #define posição do rectangulo
        self.pos = (pos_x < maxX and pos_x > minX and pos_y > minY and pos_y < maxY)
        self.card = card
        self.x = x
        self.y = y
        self.xlenght = xlenght
        self.ylenght = ylenght
        
        
        #se for uma card
        if (self.card):
            #muda cor quando a posicao é True
            c = color
            if (self.pos):
                c = colorOver
                if (mb[0]):
                    c = black
                    
            pygame.draw.rect(screen, c, (x, y, xlenght, ylenght), 0)
            
                
        #se nao for uma card
        else:
            #muda cor quando a posicao é True
            c = color
            if (self.pos):
                c = colorOver
            #desenha rectangulo
            pygame.draw.rect(screen, c, (x, y, xlenght, ylenght), 2)
            #define texto e cor
            self.text = myFont.render(textInput, True, c)
            self.writeText = screen.blit(self.text,(x+32.5,y+3.5))




class geoForm:

    def __init__(self, forms, colors, x, y, pos):
      
        self.forms = forms
        self.colors = colors
        self.pos = pos
    
        mb = pygame.mouse.get_pressed()
 
        
        if (self.pos):
            if (mb[0]):
                #cria as formas(consoante a lista criada) e dá-lhes cores
                if (forms == 'square'):
                    pygame.draw.rect(screen, colors, (x, y, 50, 50), 0)
                elif (forms == 'triangle'):
                    pygame.draw.polygon(screen, colors, [(x+23.5, y-5), (x-5, y+45), (x+50, y+45)], 0)
                elif (forms == 'circle'):
                    pygame.draw.circle(screen, colors, (25+x, 25+y), 30, 0)
            


