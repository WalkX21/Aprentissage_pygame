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



i = randint(1,4)
clock = pygame.time.Clock()





while True:
    pygame.display.update()
    
    clock.tick(40)
