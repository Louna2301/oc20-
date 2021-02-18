"""Place multiple rectangles with the mouse."""

import pygame
from pygame.locals import *

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((640, 240))

start = (0, 0)
size = (0, 0)
drawing = False
rect_list = []

# Définir une classe de forme (shape) avec un rectangle, couleur, épaisseur 
class Shape: 
    def __init__(self, rect, color=RED, width = 1): 
        self.rect = rect
        self.color = color
        self.width = width

# Créer une instance (objet) 
s = Shape(pygame.Rect(10, 10, 100, 50))

# Afficher des attributs de cet objet 
print('rect =' s.rect)
print('couleur=' s.color)
print('épaisseur=' s.width) 
        

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0]-start[0], end[1]-start[1]
            rect = pygame.Rect(start, size)
            rect_list.append(rect)
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0]-start[0], end[1]-start[1]

    screen.fill(GRAY)
    for shape in shape_list:
        pygame.draw.rect(screen, shape.color, shape.rect, shape.width )
    pygame.draw.rect(screen, BLUE, (start, size), 1)
    pygame.display.update()

pygame.quit()