import pygame
import math

# Initialisation de pygame
pygame.init()

# Définition des couleurs et de la fenêtre
back = (200, 255, 255)
mw = pygame.display.set_mode((500, 500))
mw.fill(back)
clock = pygame.time.Clock()

# Position initiale de la plateforme
platform_x = 200
platform_y = 330

# Vitesse de déplacement de la plateforme
dx = 3
dy = 3

# Flags pour le mouvement de la plateforme
move_right = False
move_left = False

# Initialisation de la variable de fin de jeu
game_over = False

# Classe pour créer des objets rectangulaires dans le jeu
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

# Classe pour créer des objets image dans le jeu
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

# Création de la balle et de la plateforme
ball = Picture('/Users/mbm/Desktop/Aprentissage_pygame/Arkanoid/ball.png', 225, 250, 50, 50)
platform = Picture('/Users/mbm/Desktop/Aprentissage_pygame/Arkanoid/platform.png', platform_x, platform_y, 100, 30)

# Création des monstres
monsters = []

# Position du cercle de monstres
circle_center_x = 250
circle_center_y = 250
rayon = 200
nombre_monstres = 12

# Calcul de l'angle entre chaque monstre
angle_interval = 360 / nombre_monstres

# Création des monstres formant le cercle
for i in range(nombre_monstres):
    angle = i * angle_interval
    x = circle_center_x + rayon * math.cos(math.radians(angle))
    y = circle_center_y + rayon * math.sin(math.radians(angle))

    monster = Picture('/Users/mbm/Desktop/Aprentissage_pygame/Arkanoid/enemy.png', x - 25, y - 25, 50, 50)
    monsters.append(monster)



# Ajout du grand monstre au milieu
grand_monstre = Picture('/Users/mbm/Desktop/Aprentissage_pygame/Arkanoid/enemy1.png', 200,200, 200, 200)
monsters.append(grand_monstre)

while not game_over:
    ball.fill()
    platform.fill()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
    
    if move_right:
        platform.rect.x += 3
    if move_left:
        platform.rect.x -= 3
    
    ball.rect.x += dx
    ball.rect.y += dy
    
    # Rebondissement sur les bords de la fenêtre
    if ball.rect.top <= 0 or ball.rect.bottom >= 500:
        dy *= -1
    if ball.rect.left <= 0 or ball.rect.right >= 500:
        dx *= -1

    # Rebondissement sur la plateforme
    if ball.rect.colliderect(platform.rect):
        dy *= -1
    
    for m in monsters:
        m.draw()
    platform.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)
