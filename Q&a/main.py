import sys

import pygame
from pygame.locals import QUIT
from random import randint

pygame.init()
#DISPLAYSURF = pygame.display.set_mode((400, 300))
#pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()
back = (134, 245,198)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)

BLACK = (0, 0, 0)
LIGHT_BLUE = (200, 200, 255)


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

        
# create cards

quest_card = TextArea(120,100,290,70,LIGHT_BLUE)
quest_card.set_text("Question",75)

ans_card = TextArea(120,240,290,70,LIGHT_BLUE)
ans_card.set_text("Answer",75)




while True:
    pygame.display.update()
    quest_card.draw(10,10)
    ans_card.draw(10,10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            # n'importe quelle touche de defini en dessous

            if event.key == pygame.K_q:

                num = randint(1, 3)
                if num == 1:
                    quest_card.set_text('la capital guyanne fr ?',25)
                
                if num == 2: 
                    quest_card.set_text("c'est quoi un port vga ?",25)
                
                if num == 3:
                    quest_card.set_text("la couleur du ciel ?",25)

                

                quest_card.draw(10,25)

            if event.key == pygame.K_a:

                num = randint(1,3)
                if num == 1:
                    ans_card.set_text('cayenne', 35)

                if num == 2:
                    ans_card.set_text('video', 35)
                
                if num == 3:
                    ans_card.set_text('bleu', 35)


                ans_card.draw(10, 25)
    clock.tick(40)


                



        

    