import pygame

class Card:
    def __init__ (self, x, y, xlenght, ylenght):
        pos_x, pos_y = pygame.mouse.get_pos()
        self.pos = (pos_x > x and pos_x < x + xlenght and pos_y > y and pos_y < y + ylenght)
        self.x = x
        self.y = y
        self.xlenght = xlenght
        self.ylenght = ylenght
        self.isClicked = False
        self.isClickable = True

    def isAt(self, mouseX, mouseY):
        self.mouseX = mouseX
        self.mouseY = mouseY
        posicao = mouseX > self.x and mouseX < self.x + self.xlenght and mouseY > self.y and mouseY < self.y + self.ylenght
        return posicao
        
    def draw (self, screen, color, border):
        self.screen = screen
        self.border = border
        self.color = color
        pygame.draw.rect(self.screen, color, (self.x, self.y, self.xlenght, self.ylenght), self.border)

    def form (self, screen, geoForm, geoColor, x, y):
        self.geoForm = geoForm
        self.geoColor = geoColor
        self.screen = screen
        if (geoForm == 'square'):
            pygame.draw.rect(self.screen, geoColor, (self.x, self.y, self.xlenght, self.ylenght), 1)
            pygame.draw.rect(self.screen, self.geoColor, (x, y, 50, 50), 0)
        elif (geoForm == 'triangle'):
            pygame.draw.rect(self.screen, geoColor, (self.x, self.y, self.xlenght, self.ylenght), 1)
            pygame.draw.polygon(self.screen, self.geoColor, [(x+25, y), (x, y+50), (x+50, y+50)], 0)
        elif (geoForm == 'circle'):
            pygame.draw.rect(self.screen, geoColor, (self.x, self.y, self.xlenght, self.ylenght), 1)
            pygame.draw.circle(self.screen, self.geoColor, (25+x, 25+y), 30, 0)


class Text:
    def __init__ (self, x, y, xlenght, ylenght):
        pos_x, pos_y = pygame.mouse.get_pos()
        self.pos = (pos_x > x and pos_x < x + xlenght and pos_y > y and pos_y < y + ylenght)
        self.x = x
        self.y = y
        self.xlenght = xlenght
        self.ylenght = ylenght
        self.isClicked = False

    def isAt(self, mouseX, mouseY):
        self.mouseX = mouseX
        self.mouseY = mouseY
        posicao = mouseX > self.x and mouseX < self.x + self.xlenght and mouseY > self.y and mouseY < self.y + self.ylenght
        return posicao
        
    def draw (self, screen, color, border, textInput):
        myFont = pygame.font.Font(pygame.font.get_default_font(), 21)
        self.screen = screen
        self.border = border
        self.textInput = textInput
        self.color = color
    
        pygame.draw.rect(self.screen, color, (self.x, self.y, self.xlenght, self.ylenght,), self.border)
        self.text = myFont.render(self.textInput, True, color)
        if textInput == 'Exit':
            self.writeText = screen.blit(self.text,(self.x+29.5,self.y+5))
        elif textInput == 'Show All':
            self.writeText = screen.blit(self.text,(self.x+6,self.y+5))
        else:
            self.writeText = screen.blit(self.text,(self.x+32,self.y+5))


