import pygame
from pygame.locals import *

SIZE = 1500, 1500
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

img = pygame.image.load('mariosurpris.jpg')
img.convert()

rect = img.get_rect()
rect.center = 600, 20
moving = False

class Shape:
    def __init__(self, rect, type_ = 'r'):
        self.rect = img
        self.type_ = type_
        
    def draw(self):
        if self.type == 'r':
            pygame.draw.rect(screen, self.rect)
        
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            if event.key == K_e:
                type_ = 'e'
