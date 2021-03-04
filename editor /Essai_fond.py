import pygame
from pygame.locals import *
import time


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

img_1 = pygame.image.load('mariosurpris.jpg')
img_1.convert()
img_1 = pygame.transform.scale(img_1, (300, 300))
img_2 = pygame.image.load('Boser.png')
img_2.convert()
img_2 = pygame.transform.scale(img_2, (400, 400))
img_3 = pygame.image.load('mariopaysage.jpg')
img_3.convert()

sysfont = pygame.font.get_default_font()
print('system font :', sysfont)
font = pygame.font.SysFont(None, 24)
img = font.render('hello', True, BLUE)
screen.blit(img, (20, 20))
t0 = time.time()
text_1 = (30, 50)   
font = pygame.font.SysFont(None, 48)
print('time needed for Font creation :', time.time()-t0)
fonts = pygame.font.get_fonts()
print(len(fonts))

font1 = pygame.font.SysFont('chalkduster.ttf', 190)
img1 = font1.render('MARIO JUMPING', True, BLUE)

font2 = pygame.font.SysFont('didot.ttc', 102)
img2 = font2.render('PLAY', True, WHITE)

rect_1 = img_1.get_rect()
rect_1.center = 400, 500

rect_2 = img_2.get_rect()
rect_2.center = 1000, 500

rect_3 = img_3.get_rect()
rect_3.center = 600, 20


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
            elif event.key == pygame.K_o:
               background = MAGENTA
                
                
    caption = 'background color = ' + str(background)
    pygame.display.set_caption(caption)
    screen.fill(background)
        
    screen.blit(img1, (150, 100))
    screen.blit(img2, (620, 700))
    
    screen.blit(img_1, rect_1)
    screen.blit(img_2, rect_2)

    pygame.display.update()

pygame.quit()