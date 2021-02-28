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
screen=pygame.display.set_mode((640, 480))
screen.fill(GREEN)
pygame.display.update() # est nécessaire pour afficher les changements

# Boucle principale (event loop)
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
            pygame.display.update()
        
pygame.quit()