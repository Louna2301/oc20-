import pygame
from pygame.locals import *

SIZE = 1500, 1500
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

img = pygame.image.load('mariosurpris.jpg')
img.convert()
img = pygame.transform.scale(img, (300, 300))
img_2 = pygame.image.load('Boser.png')
img_2.convert()
img_2 = pygame.transform.scale(img_2, (400, 400))

rect = img.get_rect()
rect.center = 400, 500
moving = False
running = True

rect_2 = img_2.get_rect()
rect_2.center = 1000, 500
moving = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect, 2)
    screen.blit(img, rect)
    screen.blit(img_2, rect_2)
    pygame.display.flip()

pygame.quit()