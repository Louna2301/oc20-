import pygame
from pygame.locals import *

SIZE = 1500, 1500
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

img = pygame.image.load('mariopaysage.jpg')
img.convert()

rect = img.get_rect()
rect.center = 600, 20
moving = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect, 2)
    screen.blit(img, rect)
    pygame.display.flip()

pygame.quit()