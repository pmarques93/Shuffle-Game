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
        
    def draw (self, screen, color, colorOver, border):
        self.screen = screen
        self.border = border
    
        c = color
        if self.pos:
            c = colorOver
        pygame.draw.rect(self.screen, c, (self.x, self.y, self.xlenght, self.ylenght,), self.border)
        
        

    def form (self, screen, form, color, x, y):
        self.form = form
        self.color = color
        self.screen = screen
        if (form == 'square'):
            pygame.draw.rect(self.screen, self.color, (x, y, 50, 50), 0)
        elif (form == 'triangle'):
            pygame.draw.polygon(self.screen, self.color, [(x+23.5, y-5), (x-5, y+45), (x+50, y+45)], 0)
        elif (form == 'circle'):
            pygame.draw.circle(self.screen, self.color, (25+x, 25+y), 30, 0)
    

class Text:
    def __init__ (self, x, y, xlenght, ylenght):
        pos_x, pos_y = pygame.mouse.get_pos()
        self.pos = (pos_x > x and pos_x < x + xlenght and pos_y > y and pos_y < y + ylenght)
        self.x = x
        self.y = y
        self.xlenght = xlenght
        self.ylenght = ylenght
        self.isClicked = False
        
    def draw (self, screen, color, colorOver, border, textInput):
        myFont = pygame.font.SysFont('Arial', 23)
        self.screen = screen
        self.border = border
        self.textInput = textInput
    
        c = color
        if self.pos:
            c = colorOver
        pygame.draw.rect(self.screen, c, (self.x, self.y, self.xlenght, self.ylenght,), self.border)
        self.text = myFont.render(self.textInput, True, c)
        self.writeText = screen.blit(self.text,(self.x+32.5,self.y+3.5))


