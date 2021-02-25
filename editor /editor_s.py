import pygame
from pygame.locals import *

# Mettre un fond (Mario paysage)
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
    
img_2 = pygame.image.load('mariosurpris.jpg')
img_2.convert()
img_2 = pygame.transform.scale(img_2, (300, 300))
img_3 = pygame.image.load('Boser.png')
img_3.convert()
img_3 = pygame.transform.scale(img_3, (400, 400))

rect_2 = img_2.get_rect()
rect_2.center = 400, 500
moving = False
running = True

rect_3 = img_3.get_rect()
rect_3.center = 1000, 500
moving = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect, 2)
    screen.blit(img_2, rect_2)
    screen.blit(img_3, rect_3)
    pygame.display.flip()

pygame.quit()