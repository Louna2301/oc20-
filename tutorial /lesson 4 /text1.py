"""Edit text with the keyboard."""
import pygame
from pygame.locals import *
import time
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((640, 140))

text = 'Bla Bla Bla Bla Bla'
font = pygame.font.SysFont(None, 48)
img = font.render(text, True, RED)

rect = img.get_rect()
rect.topleft = (60, 60)
cursor = Rect(rect.topright, (3, rect.height))

running = True
background = GRAY

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                if len(text)>0:
                    text = text[:-1]
            else:
                text += event.unicode
            img = font.render(text, True, RED)
            rect.size=img.get_size()
            cursor.topleft = rect.topright
    
    screen.fill(background)
    screen.blit(img, rect)
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, RED, cursor)
    pygame.display.update()

pygame.quit()