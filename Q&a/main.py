import pygame
import time
pygame.init()
back = (134, 245,198)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)


#colors
BLACK = (0, 0, 0)
LIGHT_BLUE = (200, 200, 255)


class TextArea():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
    
    def set_text(self, text, fsize=12, text_color=BLACK):
        self.text = text
        self.image = pygame.font.Font(None, fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + self.shift_x, self.rect.y + shift_y) )

        




