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
img1 = font1.render('MARIO THE GAME', True, BLUE)

font2 = pygame.font.SysFont('didot.ttc', 102)
img2 = font2.render('PLAY', True, WHITE)

rect_1 = img_1.get_rect()
rect_1.center = 400, 500

rect_2 = img_2.get_rect()
rect_2.center = 1000, 500


rect = Rect(100, 50, 50, 50)
width = 500
height = 500
v = [2, 2]

running = True

while running:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:# cliquer sur le bouton rouge
            running = False
        
        elif event.type == pygame.KEYDOWN: # une touche à été pressée
            print(event)
            if event.key == pygame.K_r:
                background = RED
            elif event.key == pygame.K_g:
                background = GREEN
            elif event.key == pygame.K_s:
                background = BLACK
        
               
            elif event.key == pygame.K_p:
                img2 = font2.render('PLAY', True, CYAN)
            elif event.key == pygame.K_m:
                img2 = font2.render('PLAY', True, WHITE)
       
    caption = 'background color = ' + str(background)
    pygame.display.set_caption(caption)
    screen.fill(background)
        
    screen.blit(img1, (150, 100))
    screen.blit(img2, (620, 700))
    
    screen.blit(img_1, rect_1)
    screen.blit(img_2, rect_2)

    pygame.display.update()

pygame.quit()

#Nouvelle fenêtre
pygame.init()
SIZE = 1500, 1500
screen = pygame.display.set_mode(SIZE)
screen.fill(GRAY)
pygame.display.update() # est nécessaire pour afficher les changements

import pygame
from pygame.locals import *

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)

start = (0, 0)
size = (0, 0)
drawing = False
color = RED
width = 1
type_='r'
shapes = []

# définir une classe de formes (shape) avec rectangle, couleur, épaisseur
# type_ 'r' = rectangle, 'e' = ellipse
class Shape:
    def __init__(self, rect, color=RED, width=1, type_ = 'r'):
        self.rect = rect
        self.color = color
        self.width = width
        self.type = type_
        
    def draw(self):
        if self.type == 'r':
            pygame.draw.rect(screen, self.color, self.rect, self.width)
        elif self.type == 'e':
            pygame.draw.ellipse(screen, self.color, self.rect, self.width)
            

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_0:
                width = 0
            elif event.key == K_1:
                width = 1
            elif event.key == K_2:
                width = 3
        
            elif event.key == K_r:
                color = RED
            elif event.key == K_g:
                color = GREEN
            elif event.key == K_b:
                color = BLUE
                
            elif event.key == K_e:
                type_ = 'e'
            elif event.key == K_f:
                type_ = 'r'
            
            shapes[-1].width = width
            shapes[-1].color = color
            shapes[-1].type = type_

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            s = Shape(Rect(start, (0, 0)), color, width)
            shapes.append(s)
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0]-start[0], end[1]-start[1]
            shapes[-1].rect.size = size

    screen.fill(GRAY)
    for s in shapes:
        s.draw()    
    pygame.display.update()

pygame.quit()