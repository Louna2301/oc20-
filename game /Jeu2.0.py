import pygame
pygame.init()

# fenetre du jeu
pygame.display.set_caption('Pong') 
screen = pygame.display.set_mode((950, 720))

# arrière plan du jeu
background = pygame.image.load('images2.0/background.png')

running = True

# boucle tant que la condition est vrai
while running:
    
    # appliquer l'arriere plan du jeu
    screen.blit(background, (-5, 0))
    
    # mettre a jour l'ecran
    pygame.display.flip()
    
    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # evenement est la fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()