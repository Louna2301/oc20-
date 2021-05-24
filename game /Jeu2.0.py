import pygame

pygame.init()

# fenetre du jeu
pygame.display.set_caption('Pong') 
screen = pygame.display.set_mode((1080, 720))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
pygame.quit()

