from variables import *

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
        self.beingClicked = False
        self.score = 0

    def isAt(self, mouseX, mouseY):
        posicao = mouseX > self.x and mouseX < self.x + self.xlenght and mouseY > self.y and mouseY < self.y + self.ylenght
        return posicao
        
    def draw (self, screen, color, border):

        pygame.draw.rect(screen, color, (self.x, self.y, self.xlenght, self.ylenght), border)

    def form (self, screen, geoForm, geoColor, x, y):
        self.geoForm = geoForm
        self.geoColor = geoColor
        if (geoForm == 'square'):
            pygame.draw.rect(screen, geoColor, (self.x, self.y, self.xlenght, self.ylenght), 1)
            pygame.draw.rect(screen, self.geoColor, (x, y, 50, 50), 0)
        elif (geoForm == 'triangle'):
            pygame.draw.rect(screen, geoColor, (self.x, self.y, self.xlenght, self.ylenght), 1)
            pygame.draw.polygon(screen, self.geoColor, [(x+25, y), (x, y+50), (x+50, y+50)], 0)
        elif (geoForm == 'circle'):
            pygame.draw.rect(screen, geoColor, (self.x, self.y, self.xlenght, self.ylenght), 1)
            pygame.draw.circle(screen, self.geoColor, (25+x, 25+y), 30, 0)
    
    def smallForm(self, screen, geoForm, geoColor, x, y):
        self.geoForm = geoForm
        self.geoColor = geoColor
        if (geoForm == 'square'):
            pygame.draw.rect(screen, geoColor, (self.x, self.y, self.xlenght, self.ylenght), 1)
            pygame.draw.rect(screen, self.geoColor, (x, y, 40, 40), 0)
        elif (geoForm == 'triangle'):
            pygame.draw.rect(screen, geoColor, (self.x, self.y, self.xlenght, self.ylenght), 1)
            pygame.draw.polygon(screen, self.geoColor, [(x+20, y), (x, y+35), (x+40, y+35)], 0)
        elif (geoForm == 'circle'):
            pygame.draw.rect(screen, geoColor, (self.x, self.y, self.xlenght, self.ylenght), 1)
            pygame.draw.circle(screen, self.geoColor, (20+x, 20+y), 20, 0)       

class Text(Card):
    def draw (self, screen, color, border, textInput):
        myFont = pygame.freetype.Font("fonts/NotoSans-Regular.ttf", 21)
        pygame.draw.rect(screen, color, (self.x, self.y, self.xlenght, self.ylenght,), border)

        if textInput == 'Exit':
            self.text = myFont.render_to(screen, (self.x+35, self.y+6), textInput, color)
        elif textInput == 'help':
            self.text = myFont.render_to(screen, (self.x+32, self.y+6), textInput, color)
        elif textInput == 'Hardcore':
            self.text = myFont.render_to(screen, (self.x+9, self.y+6), textInput, color)
        else:
            self.text = myFont.render_to(screen, (self.x+17, self.y+6), textInput, color)


