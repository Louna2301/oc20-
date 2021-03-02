import pygame
from pygame.locals import *


#Tools > install pygame
#Find pygame
#Install

# Definition de couleurs
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Definition de variables
background = GRAY
key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
    K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

print(key_dict)

# Initialiser le module pygame
pygame.init()

# Créer une nouvelle fenêtre
SIZE = 1500, 1500
screen = pygame.display.set_mode(SIZE)
screen.fill(GREEN)
pygame.display.update() # est nécessaire pour afficher les changements

img = pygame.image.load('mariosurpris.jpg')
img.convert()
img = pygame.transform.scale(img, (300, 300))
img_2 = pygame.image.load('Boser.png')
img_2.convert()
img_2 = pygame.transform.scale(img_2, (400, 400))
img_3 = pygame.image.load('mariopaysage.jpg')
img.convert()

# Boucle principale (event loop)
rect = img.get_rect()
rect.center = 400, 500
moving = False
running = True

rect_3 = img_3.get_rect()
rect_3.center = 600, 20
moving = False

rect_2 = img_2.get_rect()
rect_2.center = 1000, 500
moving = False
running = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# cliquer sur le bouton rouge
            running = False
        
        elif event.type == pygame.KEYDOWN: # une touche à été pressée
            print(event)
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_g:
                background = GREEN
            elif event.key == pygame.K_s:
                background = BLACK
                
    caption = 'background color = ' + str(background)
    pygame.display.set_caption(caption)
    screen.fill(background)
    screen.blit(img, rect)
    screen.blit(img_2, rect_2)
    pygame.display.flip()   
        
pygame.quit()