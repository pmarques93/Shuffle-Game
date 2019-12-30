import pygame

pygame.init()
pygame.font.init()

############ variaveis globais ###############

global x

################# colors #####################

global white, green, orange, blue, black, yellow

white = (255,255,255)
green = (0  , 150, 0)
orange = (255, 140, 0)
blue = (0, 0, 150)
black = (0, 0, 0)
yellow = (255,255,  0)

##############################################

##############   funcoes    ##################

def compare(form1, form2):
    if (form1 == form2):
        print (" --- Equal ---")
        return True
    else:
        print (" --- Not Equal ---")
        return False


    
            





