#import pygame

#pygame.init()

#back = (154, 196, 248)
#w = pygame.display.set_mode((500, 500))
#w.fill(back)

#while True:
#    pass
import sys
import time
import pygame
from pygame.locals import QUIT
from random import randint

pygame.init()

clock = pygame.time.Clock()
back = (154, 196, 248)
mw = pygame.display.set_mode((850, 720))
mw.fill(back)

BLACK = (35, 22, 81)
LIGHT_BLUE = (215, 217, 177)


class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    
    def set_text(self, text, fsize=12, text_color=BLACK):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color) #.render pr le texte

    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y) )




timer1 = pygame.time.Clock()

point1 = 0

cards = []
num_cards = 4
pizza = "clic"
x = 50

for i in range(num_cards):
    new_card=TextArea(x,100,150,250,LIGHT_BLUE)
    new_card.set_text(pizza,50)
    cards.append(new_card)
    x = x + 200
    

#quest_card = TextArea(50,100,150,250,LIGHT_BLUE)
#quest_card.set_text("",50)

#quest_card1 = TextArea(250,100,150,250,LIGHT_BLUE)
#quest_card1.set_text("",50)

#quest_card2 = TextArea(450,100,150,250,LIGHT_BLUE)
#quest_card2.set_text("",50)

# quest_card3 = TextArea(650,100,150,250,LIGHT_BLUE)
# quest_card3.set_text("",50)

timer = TextArea(250,400,150,100,LIGHT_BLUE)
timer.set_text("Timer: "+str(timer1),50)

point = TextArea(450,400,150,100,LIGHT_BLUE)
point.set_text("pts: "+str(point1),50)






while True:
    pygame.display.update()

    
    
    
    # quest_card.draw(10,10)
    # quest_card1.draw(10,10)
    # quest_card2.draw(10,10)
    # quest_card3.draw(10,10)
    timer.draw(10,10)
    point.draw(10,10)

    for new_card in cards:
        new_card.draw(10,30)




    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    
    clock.tick(40)

